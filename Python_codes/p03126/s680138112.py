N,M = map(int, input().split())

A=[]
for i in range(N):
  x = [int(i) for i in input().split()]
  A = A + x[1:]

ans = 0
from collections import Counter
for k,v in Counter(A).items():
  # print(k,v)
  if v==N: ans += 1

print(ans)
