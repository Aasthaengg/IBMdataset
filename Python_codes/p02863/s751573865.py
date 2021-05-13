n,t = map(int,input().split())
a,b = [],[]
for i in range(n):
    x,y = map(int,input().split())
    a.append(x)
    b.append(y)
dp1 = [[0]*(t+1) for _ in range(n+2)]
dp2 = [[0]*(t+1) for _ in range(n+2)]
for i in range(1,n+1):
    w,v = a[i-1],b[i-1]
    for j in range(1,t+1):
        if j < w:
            dp1[i][j] = dp1[i-1][j]
        else:
            dp1[i][j] = max(dp1[i-1][j], dp1[i-1][j-w]+v)
for i in range(n,0,-1):
    w,v = a[i-1],b[i-1]
    for j in range(1,t+1):
        if j < w:
            dp2[i][j] = dp2[i+1][j]
        else:
            dp2[i][j] = max(dp2[i+1][j], dp2[i+1][j-w]+v)


ans = 0
for i in range(1,n+1):
    for j in range(t):
        ans = max(ans,dp1[i-1][j]+dp2[i+1][t-1-j]+b[i-1])
print(ans)