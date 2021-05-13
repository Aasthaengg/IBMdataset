n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

a.sort()
b.sort()
c.sort()
from bisect import bisect_left
from bisect import bisect_right
count = 0
for bi in range(n):
  c_right = bisect_right(c, b[bi])
  a_left = bisect_left(a, b[bi])
  count += (n-c_right) * a_left
print(count)