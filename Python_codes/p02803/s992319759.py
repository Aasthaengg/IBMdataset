H, W = map(int, input().split())

S = [["#"] * (W + 2) for i in range(H + 2)]
for i in range(H):
    s = input()
    for j in range(W):
        S[i + 1][j + 1] = s[j]
#print(S)

g = H * W

d = [[float("INF")] * g for i in range(g)]
for i in range(g):
    d[i][i] = 0

for i in range(1, H + 1):
    for j in range(1, W + 1):
        if S[i][j] == ".":
            p = (i - 1)*W + (j - 1)
            if S[i][j+1] == ".":
                d[p][p + 1] = 1
            if S[i][j-1] == ".":
                d[p][p - 1] = 1
            if S[i+1][j] == ".":
                d[p][p + W] = 1
            if S[i-1][j] == ".":
                d[p][p - W] = 1

for k in range(g):
    for i in range(g):
        for j in range(g):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

ans = 0

for i in range(g):
    for j in range(g):
        if d[i][j] != float("INF"):
            ans = max(ans, d[i][j])

print(ans)