import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())

from heapq import heappush, heappop
Q = []
for _ in range(N):
    x, l = mapint()
    heappush(Q, (x+l, x-l))

ans = 0
now = -10**20
while Q:
    r, l = heappop(Q)
    if l<now:
        continue
    ans += 1
    now = r

print(ans)