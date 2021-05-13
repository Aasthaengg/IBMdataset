n,m,x=map(int,input().split())
l=[list(map(int, input().split())) for _ in range(n)]

ans=[]
for i in range(2**n):
    t=[0]*m
    cost=0
    for j in range(n):
        if (((i>>j)&1)==1):
            for k in range(m):
                t[k]+=l[j][k+1]
            cost+=l[j][0]
    
    #print('i',i,bin(i),min(t),cost)
    if min(t)>=x:
        ans.append(cost)

if len(ans)==0:
    print(-1)
else:
    print(min(ans))