n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=0
for i in range(n):
  ans+=min(a[i],b[i])
  if b[i]-a[i]>0:
    ans+=min(b[i]-a[i],a[i+1])
    a[i+1]-=min(b[i]-a[i],a[i+1])
print(ans)