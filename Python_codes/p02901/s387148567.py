N,M=map(int,input().split())
key=[]
cost=[]
for i in range(0,M):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    s=sum(2**(c[j]-1) for j in range(0,b))
    key.append(s)
    cost.append(a)

node=2**N

dp=[[10**10 for i in range(0,node)] for j in range(0,M)]

for i in range(0,M):
    dp[i][node-1]=0
#i:何番までか j:手に入れた鍵
for i in range(0,M):
    for j in range(1,node):
        k=node-1-j
        if i==0:
            if k|key[0]==node-1:
                dp[0][k]=cost[0]
        else:
            dp[i][k]=min(dp[i-1][k],dp[i-1][k|key[i]]+cost[i])

if dp[M-1][0]>=10**10:
    print(-1)
else:
    print(dp[M-1][0])