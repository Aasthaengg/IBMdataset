N = int(input())
C = [int(input()) for i in range(N)]
MOD = 10**9+7

A = []
for c in C:
    if A and A[-1]==c: continue
    A.append(c)

last = [-1] * 200001
B = [-1] * len(A)
for i,a in enumerate(A):
    B[i] = last[a]
    last[a] = i

dp = [0] * (len(A))
dp[0] = 1
for i in range(1,len(A)):
    bk = 0 if B[i] < 0 else dp[B[i]]
    dp[i] = (dp[i-1] + bk) % MOD
print(dp[-1])