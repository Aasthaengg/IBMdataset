n,m=map(int,input().split())

edge=[0]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    a,b=min(a,b),max(a,b)
    edge[a]+=1
    edge[b]-=1

for i in range(1,n+1):
    edge[i]+=edge[i-1]

for i in range(1,n):
    if edge[i]%2==1:
        print('NO')
        break
else:
    print('YES')