import bisect
import math

n = int(input())
a = list(map(int,input().split()))

a.sort()

n1 = math.ceil(math.log(1000000000,2))+1

s = [0 for _ in range(n)]
s[0] = a[0]
for i in range(1,n) :
  s[i] = s[i-1]+a[i]

ans = 0
for i in range(n) :
  h = 0
  m = a[i]*2
  for j in range(n1) :
    mg = bisect.bisect_left(a,m)
    if mg <= n-1 and m == a[mg] :
      mg += 1
    m = s[mg-1]*2
    if m >= a[n-1] :
      ans += 1
      break
  
print(ans)