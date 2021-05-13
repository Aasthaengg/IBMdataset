import sys
sys.setrecursionlimit(10 ** 7)
h, w = map(int, input().split())
s = [input() for i in range(h)]
t = [[None] * w for i in range(h)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def dfs(i, j, bw):
    global h, w
    if not (0 <= i < h and 0 <= j < w) or s[i][j] == bw or t[i][j]:
        return 0, 0
    t[i][j] = True
    W, b = 0, 0
    if s[i][j] == "#":
        b += 1
    else:
        W += 1
    for k in d:
        n, m = dfs(i + k[0], j + k[1], s[i][j])
        W += n
        b += m
    return W, b
ans = 0
for i in range(h):
    for j in range(w):
        X, Y = dfs(i, j, "u shi ta pu ni chi a ku n wara")
        ans += X * Y
print(ans)