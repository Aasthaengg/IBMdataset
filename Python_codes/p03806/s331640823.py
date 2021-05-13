N,Ma,Mb = map(int,input().split())
ABC = [list(map(int,input().split())) for i in range(N)]

dp = [[[float("inf")]*(10*N+1) for i in range(10*N+1)] for j in range(N+1)]
for i in range(N+1):
    dp[i][0][0] = 0

for i in range(1,N+1):
    for A in range(10*N+1):
        for B in range(10*N+1):
            a,b,c = ABC[i-1]
            dp[i][A][B] = min(dp[i][A][B], dp[i-1][A][B], c+dp[i-1][A-a][B-b])
            
i = 1
ans = float("inf")
while i*Ma <= 10*N and i*Mb <= 10*N:
    ans = min(ans, dp[N][i*Ma][i*Mb])
    i += 1
if ans == float("inf"):
    print(-1)
else:
    print(ans)