import sys
from heapq import heapify, heappop, heappush
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

heapify(a)

while len(a) != 1:
    f = heappop(a)
    s = heappop(a)
    s %= f
    if s != 0:
        heappush(a, s)
    heappush(a, f)

print(heappop(a))
