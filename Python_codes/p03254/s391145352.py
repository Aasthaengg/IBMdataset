N,x=map(int,input().split())
a=list(map(int,input().split()))
man=[0]*N
a.sort()
ans=0
for i in range(N):
    if a[i]<=x:
        x-=a[i]
        a[i]=0
        ans+=1
    else:
        break
if ans==N:
    if x!=0:
        ans-=1
if ans<0:
    ans=0
print(ans)
