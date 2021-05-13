
n,m=map(int,input().split())
ks=[[] for i in range(m)]
for i in range(m):
    ks[i]=list(map(int,input().split()))
p=list(map(int,input().split()))
ans=0
for i in range(2**n):
    a=[0 for _ in range(n)]
    for j in range(n):
        if (i>>j)&1:
            a[j]=1
    f=0
    for j in range(m):
        x=0
        for q in range(ks[j][0]):
            
            if a[ks[j][q+1]-1]==1:
                x+=1
        if x%2==p[j]:
            f+=1
    if f==m:
        ans+=1
print(ans)
        
        
        
            
    

    
    

        
