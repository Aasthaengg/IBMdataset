n=int(input())
a=list(map(int,input().split()))
s=sum(a)
ans=float('inf')
res=0
for i in range(n-1):
  res+=a[i]
  ans=min(ans,abs(s-2*res))
print(ans)