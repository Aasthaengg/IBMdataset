from collections import deque
from heapq import *
n, k = map(int, input().split())
v = list(map(int, input().split()))

ans = 0
num = min(k, n)
for a in range(num + 1):
    for b in range(num + 1 - a):
        trash = k - (a + b)
        get = v[:a] + v[-b:] if b != 0 else v[:a]
        heapify(get)
        for _ in range(min(trash, a + b)):
            temp = heappop(get)
            if temp > 0:
                heappush(get, temp)
                break
        SUM = sum(get)
        if ans < SUM:ans = SUM
print(ans)