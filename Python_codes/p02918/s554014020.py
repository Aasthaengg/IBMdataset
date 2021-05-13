#from collections import deque
#from heapq import heapify, heappop, heappush
#from bisect import insort
#from math import gcd
#from decimal import Decimal
#mod = 1000000007
#mod = 998244353
#N = int(input())
N, K = map(int, input().split())
S = input()
#A = list(map(int, input().split()))
#flag = True
if N==1:
  print(0)
  exit()
cnt = 0
if S[0] == 'R':
  if S[1] == 'R':
    cnt += 1
if S[-1] == 'L':
  if S[-2] == 'L':
    cnt += 1
for k in range(1,N-1):
  if S[k] == 'L':
    if S[k-1] =='L':
      cnt += 1
  else:
    if S[k+1] == 'R':
      cnt += 1

ans = min(N-1, cnt+2*K)

print(ans)
#print('Yes')
#print('No')