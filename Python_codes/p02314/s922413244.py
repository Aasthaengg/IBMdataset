N,M=map(int,input().split())
C=list(map(int,input().split()))

DP=[i for i in range(N+1)]
#print(DP)
for coin in C:
    for pay in range(N+1):
        if pay-coin>=0:
            DP[pay]=min(DP[pay],DP[pay-coin]+1)
#print(DP[-1])
print(DP[-1])
