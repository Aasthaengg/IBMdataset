import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = list(mapint())

conf = 0
from heapq import heapify, heappop, heappush
As.sort(reverse=True)
m = As.pop(0)
s = As.pop(0)
conf += m
Q = []
heappush(Q, -s)
heappush(Q, -s)
for a in As:
    s = heappop(Q)
    conf -= s
    heappush(Q, -a)
    heappush(Q, -a)
print(conf)