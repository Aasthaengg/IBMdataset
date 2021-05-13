import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

x,n = map(int,input().split())
S = set(map(int,input().split()))
for i in range(100):
  if x-i not in S:
    print(x-i)
    break
  if x+i not in S:
    print(x+i)
    break