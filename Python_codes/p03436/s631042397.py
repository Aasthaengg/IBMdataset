import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    black = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#': black += 1

    q = deque([(0, 0, 0)]) # (i, j, move_count)
    dist = -1
    visited = {(0, 0)}
    while q:
        i, j, c = q.popleft()
        if i == H - 1 and j == W - 1:
            dist = c
            break
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = i + di, j + dj
            if (ni, nj) in visited: continue
            if 0 <= ni < H and 0 <= nj < W and S[ni][nj] == '.':
                q.append((ni, nj, c + 1))
                visited.add((ni, nj))

    if dist == -1:
        print(-1)
    else:
        print(H * W - black - dist - 1)


if __name__ == "__main__":
    main()
