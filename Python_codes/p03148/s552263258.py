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
counter0 = collections.Counter()
counter1 = collections.Counter()
ls0 = []
ls1 = []
base = 0
for i, (t, d) in enumerate(ls):
    if i < k:
        if counter0[t] > 0:
            heapq.heappush(ls0, (d, t))
        counter0[t] += 1
        base += d
    else:
        if t not in counter0 and t not in counter1:
            heapq.heappush(ls1, (-d, t))
            counter1[t] += 1

m = len(counter0)
res = base + m**2

for _ in range(k):
    if len(ls0) == 0 or len(ls1) == 0:
        break
    d, _ = heapq.heappop(ls0)
    base -= d
    d, _ = heapq.heappop(ls1)
    base += -d
    m += 1
    res = max(res, base + m**2)
print(res)