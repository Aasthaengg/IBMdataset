import sys
from collections import deque

input = sys.stdin.readline


def solve(H, W, A):
    WALL = - 10 ** 7
    dist = [[WALL] + [-1] * W + [WALL] for _ in range(H + 2)]
    dist[0] = dist[-1] = [WALL] * (W + 2)

    queue = deque()
    for h in range(H):
        for w in range(W):
            if A[h][w] == "#":
                dist[h + 1][w + 1] = 0
                queue.append((h + 1, w + 1))

    while queue:
        h, w = queue.popleft()
        d = dist[h][w]
        for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            y, x = h + i, w + j
            if dist[y][x] == -1:
                dist[y][x] = d + 1
                queue.append((y, x))

    res = max(map(max, dist))
    return res


def main():
    H, W = map(int, input().split())
    A = [None] * H
    for i in range(H):
        A[i] = list(input().rstrip())

    ans = solve(H, W, A)
    print(ans)


if __name__ == "__main__":
    main()
