import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = list(map(int, input().split()))

import heapq

ans = 0
heapq.heapify(a)
while a:
    t = heapq.heappop(a)
    if ans == 0:
        ans = t
        continue
    else:
        big = max(ans, t)
        small = min(ans, t)
        if big % small != 0:
            ans = big % small
            heapq.heappush(a, small)

print(ans)
