# coding: utf-8
import sys
from heapq import heapify, heappop, heappush

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# x * xをどう評価するか、heapに「おいしさ」の高い順に入れていく
N, K = lr()
TD = [lr() for _ in range(N)]
heap = []
kind = 0
happy = 0
used = set()
TD.sort(key=lambda x: x[1], reverse=True)
for t, d in TD[:K]:
    if t not in used:
        used.add(t)
        kind += 1
    else:
        heappush(heap, d)
    happy += d

cand = [happy+kind**2]
for t, d in TD[K:]:
    if not heap:
        break
    if t in used:
        continue
    h = heappop(heap)
    happy += (d-h)
    kind += 1
    used.add(t)
    cand.append(happy+kind**2)

answer = max(cand)
print(answer)
