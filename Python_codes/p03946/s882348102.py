a,b=map(int,input().split())
k=list(map(int,input().split()))

sa=0
ans=1

n=k[a-1]

for i in range(a-2,-1,-1):
    if k[i]>n:
        n=k[i]
    tmp=n-k[i]
    if tmp>sa:
        sa=tmp
        ans=1
    elif tmp==sa:
        ans+=1

    

print(ans)
