import sys
input = sys.stdin.readline
n = int(input())
chk = []
for _ in range(n):
  f = input().split()
  chk.append(int(''.join(f),2))

p = [] 
for _ in range(n):
  P = [int(i) for i in input().split()]
  p.append(P)

import collections
ans = -float('inf')
for i in range(1,2**10):
  que = 0
  for j,cj in enumerate(chk):
    d = format(i & cj,'b')
    c = collections.Counter(d)
    que += p[j][c['1']]
  ans = max(ans,que)
print(ans)