import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from collections import defaultdict

n,m = map(int,readline().split())
a = list(map(int,readline().split()))

c = [0]*(n+1)
for i in range(n):
  c[i+1] = a[i]+c[i]

d = defaultdict(int)
for i in c:
  d[i%m] += 1
  
ans = 0
for i in d.values():
  ans += (i-1)*i//2
print(ans)