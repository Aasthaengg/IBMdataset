import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n,a,b = map(int,input().split())
ans = ((n-1)*b + a) - (b + (n-1)*a) + 1
print(max(ans,0))