n=int(input())
a=list(map(int,input().split()))
for i in range(n):
  a[i]-=i
a=sorted(a)
m=a[n//2]
ans=0
for i in range(n):
  ans+=abs(a[i]-m)
print(ans)