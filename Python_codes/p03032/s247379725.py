import sys
input = sys.stdin.readline
n,k = map(int,input().split())
a = [int(i) for i in input().split()]
b = a[::-1]
ans = 0
from heapq import heapify,heappop,heappush

for l in range(1,k+1):
  ans_l = 0
  ans_r = 0
  for j in range(1,l+1):
    left = a[:j]
    chk_l = sum(left)
    heapify(left)
    heappush(left,0)
    for jj in range(l-j):
      p = heappop(left)
      if p >= 0:
        break
      chk_l -= p
    ans_l = max(ans_l,chk_l)
    
  if l < n:
    r = k-l
    for j in range(1,r+1):
      m = min(j,n-l)
      right = b[:m]
      chk_r = sum(right)
      heapify(right)
      heappush(right,0)
      for jj in range(r-m):
        q = heappop(right)
        if q >= 0:
          break
        chk_r -= q
      ans_r = max(ans_r,chk_r)
      
  ans = max(ans,ans_r+ans_l)
print(ans)