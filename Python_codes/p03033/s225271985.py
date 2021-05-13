import sys
import heapq
from collections import defaultdict
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

N, Q = map(int, input().split())
task = []
for _ in range(N):
    s, t, x = map(int, input().split())
    start = t - x
    end = s - x
    task.append((start, -1, x))
    task.append((end, 1, x))
task.sort(reverse=True)

cand = []
discard = defaultdict(int)
ans = []

for _ in range(Q):
    d = int(input())
    while task and task[-1][0] <= d:
        _, flag, x = task.pop()
        if flag == 1:
            heapq.heappush(cand, x)
        else:
            discard[x] += 1

    while cand:
        x = cand[0]
        if discard[x] > 0:
            heapq.heappop(cand)
            discard[x] -= 1
        else:
            break

    if cand:
        ans.append(cand[0])
    else:
        ans.append(-1)

print(*ans, sep="\n")