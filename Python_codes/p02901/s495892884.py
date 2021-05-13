import sys
def S(): return sys.stdin.readline().rstrip()

N,M = map(int,S().split())
AB = []
C = []
for _ in range(M):
    AB.append(tuple(int(i) for i in S().split()))
    C.append(sum(1<<(int(i)-1) for i in S().split()))

dp = [float('inf')]*(1<<N)
dp[0] = 0

for i in range(1<<N):
    for j in range(M):
        a,b = AB[j]
        c = C[j]
        dp[i|c] = min(dp[i|c],dp[i]+a)

if dp[-1] == float('inf'):
    print(-1)
else:
    print(dp[-1])