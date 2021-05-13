N = int(input())
C = [int(input()) for _ in range(N)]

mod = 10 ** 9 + 7

D = []
prev = -1
for ci in C:
    if prev != ci:
        D.append(ci)
        prev = ci

M = len(D)

dic = dict()
dp = [1] * M
for i in range(M):
    if D[i] in dic:
        temp = dp[dic[D[i]]]
        dp[i] = (dp[i - 1] + temp) % mod
    else:
        dp[i] = dp[i - 1]
    dic[D[i]] = i

print(dp[-1] % mod)

