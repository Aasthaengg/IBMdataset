import itertools

n = int(input())
a = tuple(map(int,input().split()))
ans = 0
for l in itertools.product([-1,0,1],repeat=n):
  t = 1
  for i in range(n):
    t*=(a[i]+l[i])
  if t%2==0:
    ans+=1
print(ans)