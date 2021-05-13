import sys
input = sys.stdin.readline

import math
import bisect

N,M = map(int,input().split())
S = input()

if "1"*M in S:
  print(-1)
  exit()  

S = [int(S[i]) for i in range(N+1)]

L = [(1<<i) -1 for i in range(1,M+1)]

max_n = [0]
mask = (1<<M) -1
b = 0
for i in range(N):
  b = ((b<<1) + (1- S[i])) & mask
  max_n.append(bisect.bisect_left(L,b)+1)

now = N
deme = []
while now != 0:
  x = max_n[now]
  now -= x
  deme.append(x)
print(*deme[::-1])