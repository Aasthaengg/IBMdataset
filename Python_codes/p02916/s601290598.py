#from collections import deque
#from heapq import heapify, heappop, heappush
#from bisect import insort
#from math import gcd
#from decimal import Decimal
#mod = 1000000007
#mod = 998244353
N = int(input())
#N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
#flag = True
ans = 0
b = -2
for k in range(N):
  if A[k] == b+1:
    ans += C[b-1]
  ans+=B[A[k]-1] 
  
  b = A[k]
print(ans)