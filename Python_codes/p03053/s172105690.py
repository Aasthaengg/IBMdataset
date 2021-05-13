# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
from collections import deque
def main(H, W, A):
    dist = [[-1] * W for _ in range(H)]
    q = deque()
    for i in range(H):
        for j in range(W):
            if A[i][j] == '#':
                dist[i][j] = 0
                q.append((i, j, 0))

    ans = 0
    while q:
        i, j, d = q.popleft()
        ans = max(ans, d)
        for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if not (0 <= ni < H and 0 <= nj < W): continue
            if dist[ni][nj] >= 0: continue
            dist[ni][nj] = d + 1
            q.append((ni, nj, d + 1))
    print(ans)

if __name__ == '__main__':
    input = sys.stdin.readline
    H, W = map(int, input().split())
    A = [input().rstrip() for _ in range(H)]
    main(H, W, A)
