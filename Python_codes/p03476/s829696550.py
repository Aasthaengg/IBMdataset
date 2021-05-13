from math import sqrt
from itertools import accumulate

L = [0 for _ in range(10**5)]
check = [1 for _ in range(10**5)]
check[0],check[1] = 0,0
for i in range(2,10**5):
  if check[i]:
    for j in range(i**2,10**5,i):
      check[j] = 0

for i in range(3,10**5,2):
  if check[i] == 1 and check[((i+1)//2)] == 1:
    L[i] = 1

Q = int(input())
lr = [list(map(int,input().split())) for _ in range(Q)]
ans = list(accumulate(L))
for l,r in lr:
  print(ans[r]-ans[l-1]) 