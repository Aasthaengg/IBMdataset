n,*a = map(int,open(0).read().split())
total = sum(a)
ans = 10**18
dt = 0
for i in range(n-1):
  dt += a[i]
  ans = min(ans,abs(total-dt-dt))
print(ans)