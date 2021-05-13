n,m,x,*book=map(int,open(0).read().split())
ans=10**10

for i in range(2**n):
    j=i
    k=0
    cur=0
    curskill=[0]*m
    while j>0:
        if j&1:
            cur+=book[k*(m+1)]
            for l in range(1,m+1):
                curskill[l-1]+=book[k*(m+1)+l]
        j=j>>1
        k+=1
    
    for j in range(m):
        if curskill[j]<x:
            break
    else:
        ans=min(ans,cur)

if ans==10**10:
    print(-1)
else:
    print(ans)