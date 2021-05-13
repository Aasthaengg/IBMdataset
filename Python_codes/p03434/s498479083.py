ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))
from math import ceil

n=ni()
a=nl()

sa = sorted(a)[::-1]
aa = []
bb = []
for i in range(n):
  if i%2==0:
    aa.append(sa[i])
  else:
    bb.append(sa[i])

print(sum(aa)-sum(bb))
