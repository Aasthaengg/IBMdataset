N=int(input())
a=list(map(int,input().split()))
for i in range(N):
  if i!=0:
    a[i]=a[i]+a[i-1]
ans=10**10
for i in range(N-1):
  ans=min(ans,abs(a[i]+a[i]-a[N-1]))
print(ans)