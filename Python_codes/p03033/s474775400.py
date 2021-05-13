from collections import deque, defaultdict
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
events = [None] * (2*N)
for i in range(N):
    S, T, X = map(int, input().split())
    events[2*i] = (S-X, X)
    events[2*i+1] = (T-X, -X)
events.sort(key=lambda x: x[0])
events = deque(events)
ans = [0] * Q
cur = []
remove = defaultdict(int)
for i in range(Q):
    D = int(input())
    while events and events[0][0] <= D:
        t, x = events.popleft()
        if x > 0:
            heappush(cur, x)
        else:
            remove[-x] += 1
    while cur and remove[cur[0]]:
        remove[cur[0]] -= 1
        heappop(cur)
    ans[i] = cur[0] if cur else -1
print(*ans, sep='\n')
