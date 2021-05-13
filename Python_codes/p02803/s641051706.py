def solve():
    def bfs(maze, start):
        from collections import deque

        directions = ((-1,0), (1,0), (0,-1), (0, 1))
        H = len(maze)
        W = len(maze[0])
        visited = []
        for i in range(H):
            visited.append(maze[i][:])

        nexts = deque()
        nexts.append((start, 0))
        x,y = start
        visited[x][y] = '#'
        longest_distance = 0
        while nexts:
            cur_pos,cur_distance = nexts.popleft()
            longest_distance = max(cur_distance, longest_distance)
            x,y = cur_pos
            for direction in directions:
                dx,dy = direction
                next_x = x + dx
                next_y = y + dy
                next_pos = (next_x, next_y)
                if 0 <= next_x < H and 0 <= next_y < W and next_pos:
                    if visited[next_x][next_y] == '.':
                        visited[next_x][next_y] = '#'
                        nexts.append(((next_x, next_y), cur_distance+1))
        return longest_distance

    H,W = [int(i) for i in input().split()]
    maze = []
    for i in range(H):
        row = [c for c in input()]
        maze.append(row)

    ans = 0
    for i in range(H):
        for j in range(W):
            if maze[i][j] == '.':
                start = (i,j)
                longest_distance = bfs(maze, start)
                ans = max(longest_distance, ans)

    print(ans)


if __name__ == "__main__":
    solve()