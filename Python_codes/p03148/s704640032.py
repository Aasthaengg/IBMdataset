import sys
def input():
    return sys.stdin.readline()[:-1]
from heapq import *
from collections import defaultdict
N, K = map(int, input().split())
d_t = [list(map(int, input().split()))[::-1] for i in range(N)]
d_t.sort(reverse = 1)
f, c = 0, 0
dic = defaultdict(lambda : 0)
take = []
for d, t in d_t[:K]:
    f += d
    if dic[t] == 0:
        c += 1
    dic[t] += 1
    heappush(take, [d, t])
ans = f + c * c
rest = [[-d, t] for d, t in d_t[K:]]
heapify(rest)
while take:
    d, t = heappop(take)
    if dic[t] == 1: continue
    dic[t] -= 1
    f -= d
    while rest:
        rd, rt = heappop(rest)
        if dic[rt] == 0:
            dic[rt] = 1
            c += 1
            f -= rd
            ans = max(ans, f + c * c)
            break
print(ans)
