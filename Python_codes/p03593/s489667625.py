import heapq
from collections import defaultdict
h, w = map(int, input().split())
cnt = defaultdict(int)
for _ in range(h):
    for a in input():
        cnt[a] -= 1
blocks = list(cnt.values())
heapq.heapify(blocks)

tasks = []
tasks.extend([4]*((h//2)*(w//2)))
tasks.extend([2]*((h % 2)*(w//2)+(w % 2)*(h//2)))
if h & 1 and w & 1:
    tasks.append(1)


for k in tasks:
    v = -heapq.heappop(blocks)
    if v < k:
        break
    x = -(v-k)
    if x == 0:
        continue
    heapq.heappush(blocks, x)
print('Yes' if not blocks else 'No')