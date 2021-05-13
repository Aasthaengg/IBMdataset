import collections
import heapq
import operator
import sys

input = sys.stdin.readline

ri = lambda: int(input())
rs = lambda: input().rstrip()
ril = lambda: list(map(int, input().split()))
rsl = lambda: input().rstrip().split()
ris = lambda n: [ri() for _ in range(n)]
rss = lambda n: [rs() for _ in range(n)]
rils = lambda n: [ril() for _ in range(n)]
rsls = lambda n: [rsl() for _ in range(n)]

n, k = ril()
ls = rils(n)
ls.sort(key=operator.itemgetter(1), reverse=True)
counter = collections.Counter()
ls0 = []
ls1 = []
base = 0
for i, (t, d) in enumerate(ls):
    if i < k:
        heapq.heappush(ls0, (d, t))
        counter[t] += 1
        base += d
    else:
        if t not in counter:
            heapq.heappush(ls1, (-d, t))

m = len(counter)
res = base + m**2

for i in range(k):
    ok = False
    while ls0:
        d, t = heapq.heappop(ls0)
        counter[t] -= 1
        if counter[t] > 0:
            base -= d
            ok = True
            break
    if not ok:
        break

    ok = False
    while ls1:
        d, t = heapq.heappop(ls1)
        if t not in counter:
            counter[t] += 1
            base += -d
            ok = True
            break
    if not ok:
        break

    res = max(res, base + (m + i + 1)**2)
print(res)