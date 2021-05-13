from collections import deque
mod = 10**9 + 7
N = int(input())
C = [int(input()) for i in range(N)]
dq = deque()
dq.append(C[0])
for c in C:
    if c != dq[-1]:
        dq.append(c)
C = list(dq)
N = len(C)
dp = [0]*(N+1)
dp[0] = 1
acc = [0]*(2*pow(10,5)+1)
for i in range(1,N+1):
    dp[i] = dp[i-1]
    dp[i] += acc[C[i-1]]
    dp[i] %= mod
    acc[C[i-1]] += dp[i-1]
    acc[C[i-1]] %= mod
ans = dp[N]
print(ans)