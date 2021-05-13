import sys
input = sys.stdin.readline
from collections import deque


def read():
    H, W = map(int, input().strip().split())
    S = []
    for i in range(H):
        s = list(input().strip())
        S.append(s)
    return H, W, S


def solve(H, W, S):
    n_cells = 0
    for y in range(H):
        for x in range(W):
            if S[y][x] == ".":
                n_cells += 1
    A = [[-1 for j in range(W)] for i in range(H)]
    A[0][0] = 1
    D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q = deque()
    q.append((0, 0))
    while q:
        y, x = q.popleft()
        for dy, dx in D:
            ny, nx = y + dy, x + dx
            if 0 <= ny < H and 0 <= nx < W and S[ny][nx] == "." and A[ny][nx] == -1:
                A[ny][nx] = A[y][x] + 1
                q.append((ny, nx))
    shortest = A[H-1][W-1]
    return n_cells - shortest if shortest > 0 else -1


if __name__ == '__main__':
    inputs = read()
    print(solve(*inputs))
