import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

X  = list(map(int,input().split()))
for i,xi in enumerate(X):
  if xi == 0:
    print(i+1)
    break