import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

N = int(input())
h = list(map(int,input().split()))

c2 = 0
c1 = abs(h[1] - h[0])
now = c1
for i in range(2,N):
    now = min(c2 + abs(h[i-2] -h [i]),  c1 +abs(h[i-1] -h [i]))
    c2 = c1
    c1 = now
print(now)
