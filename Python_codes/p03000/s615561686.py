N,X=map(int,input().split())
L=[int(x) for x in input().split()]
D=[0]*(N+1)
for i in range(1,N+1):
    D[i]=D[i-1]+L[i-1]
ans=0
for d in D:
    if d<=X:
        ans+=1
print(ans)
