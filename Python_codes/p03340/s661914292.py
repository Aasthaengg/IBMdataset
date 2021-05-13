n=int(input())
a=list(map(int,input().split()))
ans=s=r=0
for l in range(n):
  while r<n and s&a[r]==0:
    s+=a[r]
    r+=1
  s-=a[l]
  ans+=r-l
print(ans)