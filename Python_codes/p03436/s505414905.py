"""
Maze class.

cf. WarpableMaze class.
"""
import sys
from collections import deque
from typing import List, Tuple


class Maze:
    __slots__ = ["height", "width", "wall", "sentinel", "unsearched", "dist"]

    def __init__(
        self, height: int, width: int, grid: List[bytes], wall: str = "#",
    ) -> None:
        self.height = height + 2
        self.width = width + 2
        self.wall = -1
        self.sentinel = -2
        self.unsearched = 1 << 30
        self.dist = self._convert_grid_to_dist(grid, wall)

    def _convert_grid_to_dist(self, grid: List[bytes], wall) -> List[int]:
        """Convert a 2D grid to a 1D dist."""
        dist = [self.sentinel] * self.height * self.width
        i = self.width
        for row in grid:
            for c in row.decode():
                i += 1
                dist[i] = self.wall if c == wall else self.unsearched
            i += 2
        return dist

    def _flatten_coordinate(self, x: int, y: int) -> int:
        """Flatten 2D coordinate values.
        Values of a coordinate must be 1-origin.
        """
        return self.width * x + y

    def bfs(
        self,
        start_2d: Tuple[int, int],
        goal_2d: Tuple[int, int],
        updates_dist: bool = False,
    ) -> int:
        """BFS to compute the distance from start to goal.
        Values of start_2d and goal_2d must be 1-origin.
        """
        start = self._flatten_coordinate(*start_2d)
        goal = self._flatten_coordinate(*goal_2d)

        moves = (-self.width, self.width, -1, 1)
        dist = self.dist[:]
        dist[start] = 0
        queue = deque([start])

        while queue:
            x = queue.popleft()
            cur_dist = dist[x]
            if x == goal:
                break

            for dx in moves:
                nx = x + dx
                if dist[nx] == self.unsearched:
                    dist[nx] = cur_dist + 1
                    queue.append(nx)

        if updates_dist:
            self.dist = dist
        return dist[goal] if dist[goal] != self.unsearched else self.wall

    def debug(self) -> None:
        """Show debugging information."""

        def convert(n: int) -> str:
            if n == self.sentinel:
                return "†"
            elif n == self.wall:
                return "#"
            return "."

        print(f"<DEBUG>\nheight={self.height}, width={self.width}\n", file=sys.stderr)
        for row in zip(*[iter(self.dist)] * self.width):
            print(*map(convert, row), file=sys.stderr)


class BreakableMaze(Maze):
    def __init__(self, height: int, width: int, grid: List[bytes], wall: str = "#"):
        self.start = -1
        self.goal = -1
        super().__init__(height, width, grid, wall)

    def _convert_grid_to_dist(self, grid: List[bytes], wall) -> List[int]:
        """Convert a 2D grid to a 1D dist."""
        dist = [self.sentinel] * self.height * self.width
        i = self.width
        for row in grid:
            for c in row.decode():
                i += 1
                dist[i] = self.wall if c == wall else self.unsearched
                if c == "s":
                    self.start = i
                elif c == "g":
                    self.goal = i
            i += 2
        return dist

    def breakable_bfs(self, updates_dist: bool = False) -> int:
        """BFS to compute the distance from start to goal.
        """
        moves = (-self.width, self.width, -1, 1)
        dist = self.dist[:]
        dist[self.start] = 0
        queue = deque([self.start])

        while queue:
            x = queue.popleft()
            cur_dist = dist[x]
            if x == self.goal or cur_dist > 2:
                break

            for dx in moves:
                nx = x + dx
                if dist[nx] == self.unsearched:
                    dist[nx] = cur_dist
                    queue.appendleft(nx)
                elif dist[nx] == self.wall:
                    dist[nx] = cur_dist + 1
                    queue.append(nx)

        if updates_dist:
            self.dist = dist
        return dist[self.goal]


def abc007_c():
    # https://atcoder.jp/contests/abc007/tasks/abc007_3
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline

    R, C = map(int, readline().split())
    (*start,) = map(int, readline().split())
    (*goal,) = map(int, readline().split())
    (*S,) = read().split()

    maze = Maze(R, C, S)
    print(maze.bfs(start, goal))


def abc088_d():
    # https://atcoder.jp/contests/abc088/tasks/abc088_d
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline

    H, W = map(int, readline().split())
    (*S,) = read().split()
    maze = Maze(H, W, S)

    dist = maze.bfs((1, 1), (H, W))
    if dist != -1:
        res = H * W - sum((row.decode()).count("#") for row in S) - dist - 1
        print(res)
    else:
        print(-1)


def arc005_c():
    # https://atcoder.jp/contests/arc005/tasks/arc005_3
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline

    H, W = map(int, readline().split())
    (*C,) = read().split()
    maze = BreakableMaze(H, W, C)
    print("YES" if maze.breakable_bfs() <= 2 else "NO")


if __name__ == "__main__":
    # abc007_c()  # https://atcoder.jp/contests/abc007/tasks/abc007_3
    abc088_d()  # https://atcoder.jp/contests/abc088/tasks/abc088_d
    # arc005_c()  # https://atcoder.jp/contests/arc005/tasks/arc005_3
