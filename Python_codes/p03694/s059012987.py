n=int(input())
a=list(map(int,input().split()))
a.sort()
ans=0
now=a[0]
for i in a:
  ans+=i-now
  now=i
print(ans)