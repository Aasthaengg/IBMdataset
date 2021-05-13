import sys
sys.setrecursionlimit(10**9)
n=int(input())
a=[]
for i in range(n):
    a.append(tuple(map(int,input().split())))
#print(a)

root=[[] for i in range(n*(n-1)//2)]
buf=0
for i in range(n):
    buf=0
    for j in range(n-1):
        if j==0:
            x=min(i,a[i][j]-1)
            y=max(i,a[i][j]-1)
            buf=x*(2*n-2-x+1)//2+(y-x)-1
            #print(x,y,buf)
            continue
        x=min(i,a[i][j]-1)
        y=max(i,a[i][j]-1)
        node=x*(2*n-2-x+1)//2+(y-x)-1
        #print(x,y,node)
        root[buf].append(node)
        buf=node
flag=[True]

#閉路☑
def dfs(node,par): 
    dp[node]=0
    for item in root[node]:
        if item==par:
            continue
        if dp[item]==0:
            flag[0]=False
            return
        if dp[item]==-1: 
            dfs(item,node)
    dp[node]=1#finish
dp=[-1]*(n*(n-1)//2)
for i in range(n*(n-1)//2):
    if dp[i]==-1:
        dfs(i,i)
        if flag[0]==False:
            break
if flag[0]==False:
    print(-1)
    sys.exit()
dp=[-1]*(n*(n-1)//2)
def dfs1(node,par): 
    buf=0
    for item in root[node]:
        if item==par:
            continue
        if dp[item]!=-1:
            buf=max(buf,dp[item])
            continue
        if dp[item]==-1: 
            buf=max([buf,dfs1(item,node)])
    dp[node]=buf+1#finish
    return buf+1

for i in range(n*(n-1)//2):
    if dp[i]==-1:
        dp[i]=dfs1(i,i)
print(max(dp))

