n,m = map(int,input().split())
A = list(map(int,input().split()))
from itertools import accumulate
A = accumulate([0]+A)

A = [a % m for a in A]

lst = {}

for a in A:
  if a not in lst:
    lst[a] = 0
  lst[a] += 1
  
def comb2(n):
  return n*(n-1)//2

ans = 0
for key in lst:
  ans += comb2(lst[key])
print(ans)