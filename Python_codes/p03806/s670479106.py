N,Ma,Mb=map(int,input().split())
abc=[]
INF=float("inf")
for i in range(N):
    a,b,c=map(int,input().split())
    abc.append((a,b,c))
stack=set([(0,0)])
dp=[[[INF]*(401) for j in range(401)] for i in range(N+1)]
dp[0][0][0]=0
for i in range(N):
    dp[i+1][0][0]=0
    a,b,c=abc[i]
    stack_=set()
    for x,y in stack:
        dp[i+1][x][y]=min(dp[i][x][y],dp[i+1][x][y])
        dp[i+1][x+a][y+b]=min(dp[i+1][x+a][y+b],dp[i][x+a][y+b],dp[i][x][y]+c)
        stack_.add((x+a,y+b))
        stack_.add((x,y))
    stack=stack_
k=1
ans=INF
while(Ma*k<=400 and Mb*k<=400):
    ans=min(dp[N][Ma*k][Mb*k],ans)
    k+=1
if ans==INF:
    print(-1)
else:
    print(ans)
