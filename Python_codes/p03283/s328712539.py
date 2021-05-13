# https://atcoder.jp/contests/abc106/tasks/abc106_d

MAX_N = 505
n, m, q = map(int, input().split())
P = [[0] * MAX_N for _ in range(MAX_N)]

# 二次元累積和
for _ in range(m):
    li, ri = map(int, input().split())
    P[li][ri] += 1
for i in range(1, MAX_N):
    for j in range(1, MAX_N):
        P[i][j] += P[i][j - 1]
for i in range(1, MAX_N):
    for j in range(1, MAX_N):
        P[i][j] += P[i - 1][j]

# queryに答える
for _ in range(q):
    l, r = map(int, input().split())
    ans = P[r][r] + P[l - 1][l - 1] - P[l - 1][r] - P[r][l - 1]
    print(ans)