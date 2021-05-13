n=int(input())
f=[0]*n
p=[0]*n
INF=10**9
for i in range(n):
    f[i]=list(map(int,input().split()))
for i in range(n):
    p[i]=list(map(int,input().split()))
ans=-INF
for i in range(1,1<<10):
    cnt=0
    l=[0]*n
    for j in range(10):
        if (i>>j)%2==1:
            for h in range(n):
                if f[h][j]==1:
                    l[h]+=1
    x=0
    for i in range(n):
        x+=p[i][l[i]]
    ans=max(x,ans)
print(ans)