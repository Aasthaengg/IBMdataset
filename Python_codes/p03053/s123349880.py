import sys
from collections import deque

input = sys.stdin.readline


def bfs(H, W, A, dist):
    queue = deque([])
    for h in range(H):
        A_h = A[h]
        dist_h = dist[h]
        for w in range(W):
            if A_h[w] == "#":
                dist_h[w] = 0
                queue.append((h, w))
    while queue:
        h, w = queue.popleft()
        for y, x in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_h, next_w = h + y, w + x
            if dist[next_h][next_w] == -1:
                dist[next_h][next_w] = dist[h][w] + 1
                queue.append((next_h, next_w))


def main():
    H, W = map(int, input().split())
    A = [None] * (H + 2)
    A[0] = A[-1] = "." * (W + 2)
    for i in range(1, H + 1):
        A[i] = "".join([".", input().rstrip(), "."])

    dist = [[0] + [-1] * W + [0] for _ in range(H + 2)]
    dist[0] = dist[-1] = [0] * (W + 2)
    bfs(H + 2, W + 2, A, dist)

    ans = max(map(max, dist))
    print(ans)


if __name__ == "__main__":
    main()
