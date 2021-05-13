N=int(input())
a=list(map(int,input().split()))
s=sum(a)
if N==0:
    print(1 if a[0]==1 else -1)
    exit()
lim=1
ans=0
for i in range(N+1):
    ans+=lim
    if lim-a[i]<0:
        print(-1)
        exit()
    lim=(lim-a[i])*2
    s-=a[i]
    lim=min(lim,s)
print(ans)
