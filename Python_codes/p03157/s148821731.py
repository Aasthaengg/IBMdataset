import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
S = [list(map(lambda x: 1 if x == '#' else 0, input()[:-1])) for _ in [0]*H]
for i, ss in enumerate(S):
    for j, s in enumerate(ss):
        if (i ^ j) & 1:
            ss[j] ^= 1

visited = [0]*(H*W)

dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def dfs(i, j, cnt):
    c = S[i][j]
    for di, dj in dirs:
        ni, nj = i+di, j+dj
        if not 0 <= ni < H or not 0 <= nj < W:
            continue
        if visited[ni*W+nj]:
            continue
        if c == S[ni][nj]:
            visited[ni*W+nj] = 1
            cnt[(ni ^ nj) & 1] += 1
            dfs(ni, nj, cnt)


ans = 0
for i in range(H):
    for j in range(W):
        if visited[i*W+j]:
            continue
        visited[i*W+j] = 1
        cnt = [0, 0]
        cnt[(i ^ j) & 1] += 1
        dfs(i, j, cnt)
        ans += cnt[0] * cnt[1]
print(ans)
