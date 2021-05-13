import math

N, M = list(map(int, input().split()))

keys = []

for i in range(M):
    a, b = list(map(int, input().split()))
    key_bit = 0
    c = list(map(int, input().split()))
    for j in range(b):
        key_bit |= 1 << (c[j] - 1)
    keys.append([a, key_bit])

dp = [math.inf]*(1 << N)

dp[0] = 0

for i in range(M):
    for j in range(1 << N):
        dp[j | keys[i][1]] = min(dp[j | keys[i][1]], dp[j] + keys[i][0])

if dp[-1] == math.inf:
    dp[-1] = -1

print(dp[-1])
