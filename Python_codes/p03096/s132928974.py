import sys

N = int(input())
C = [int(sys.stdin.readline()) for _ in range(N)]
MOD = 10**9 + 7
A = []
for c in C:
    if A and A[-1] == c:
        continue
    A.append(c)
NA = len(A)
last = [-1] * 200001
B = [-1] * 200001
for i, a in enumerate(A):
    B[i] = last[a]
    last[a] = i

dp = [0] * NA
dp[0] = 1
for i in range(1, NA):
    prev = 0 if B[i] < 0 else dp[B[i]]
    dp[i] = (dp[i - 1] + prev) % MOD
print(dp[-1])