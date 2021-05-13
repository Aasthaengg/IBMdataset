n=int(input())
a=list(map(int,input().split()))
minimum=10**9
k=sum(a)
ans=0
for i in range(n):
  if abs(a[i]*n-k)<minimum:
    ans=i
    minimum=abs(a[i]*n-k)
print(ans)