import sys
from collections import deque

input = sys.stdin.readline


def solve(H, W, A):
    dist = [[0] + [-1] * W + [0] for _ in range(H + 2)]
    dist[0] = dist[-1] = [0] * (W + 2)

    queue = deque()
    for h in range(1, H + 1):
        for w in range(1, W + 1):
            if A[h][w] == "#":
                dist[h][w] = 0
                queue.append((h, w))

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
    A = [None] * (H + 2)
    A[0] = A[-1] = "." * (W + 2)
    for i in range(1, H + 1):
        A[i] = "".join((".", input().rstrip(), "."))

    ans = solve(H, W, A)
    print(ans)


if __name__ == "__main__":
    main()
