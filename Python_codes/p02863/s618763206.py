N,T = map(int,input().split())
food = [list(map(int,input().split())) for i in range(N)]

dp1 = [[0 for t in range(T+1)] for i in range(N+1)]

for i in range(1,N+1):
    time,deliciousness = food[i-1]
    for t in range(1,T+1):
        if time <= t:
            dp1[i][t] = max(dp1[i-1][t],dp1[i-1][t-time]+deliciousness)
        else:
            dp1[i][t] = dp1[i-1][t]
            
dp2 = [[0 for t in range(T+1)] for i in range(N+1)]

for i in range(N):
    time,deliciousness = food[N-i-1]
    for t in range(1,T+1):
        if time <= t:
            dp2[N-i-1][t] = max(dp2[N-i][t],dp2[N-i][t-time]+deliciousness)
        else:
            dp2[N-i-1][t] = dp2[N-i][t]

ans = 0

for t in range(T):
    for i in range(1,N+1):
        ans = max(ans,dp1[i-1][t]+dp2[i][T-1-t]+food[i-1][1])
        
print(ans)