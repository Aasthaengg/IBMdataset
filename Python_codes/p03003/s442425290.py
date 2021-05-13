n, m = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
mod = 10**9 + 7

DP = [[0] * n for _ in range(m)]

t0 = T[0]
count = 0
for i in range(n):
    if S[i] == t0:
        count += 1
    DP[0][i] = count

s0 = S[0]
count = 0
for j in range(m):
    if T[j] == s0:
        count += 1
    DP[j][0] = count

for j in range(1, m):
    for i in range(1, n):
        total = DP[j-1][i] + DP[j][i-1] - DP[j-1][i-1]
        if T[j] == S[i]:
            total += DP[j-1][i-1] + 1
        total %= mod
        DP[j][i] = total

ans = DP[m-1][n-1] + 1
print(ans)
