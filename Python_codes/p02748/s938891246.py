A,B,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=10**6
for i in range(M):
    x,y,c=map(int,input().split())
    ans=min(ans,(a[x-1]+b[y-1])-c)
a.sort(key=int)
b.sort(key=int)
for i in range(min(A,B)):
    if a[i]+b[i]>=ans: break
    ans=min(ans,a[i]+b[i])
print(ans)