import sys
def S(): return sys.stdin.readline().rstrip()

N,M = map(int,S().split())
AB = []
C = []
for _ in range(M):
    AB.append(tuple(int(i) for i in S().split()))
    C.append(sum(1<<(int(i)-1) for i in S().split()))

dp = [10**8+1]*(1<<N)
dp[0] = 0

for i in range(1<<N):
    for j in range(M):
        a,b = AB[j]
        c = C[j]
        m = i|c
        dp[m] = min(dp[m],dp[i]+a)

if dp[-1] == 10**8+1:
    print(-1)
else:
    print(dp[-1])