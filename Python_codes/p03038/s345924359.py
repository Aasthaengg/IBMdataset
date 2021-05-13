import heapq
n, m = map(int, input().split())
_a = list(map(int, input().split()))
a = [-i for i in _a]
lc = set()
bcount = dict()
heapq.heapify(a)
for i in range(m):
    b, c = map(int, input().split())
    lc.add(-c)
    if str(c) in bcount.keys():
        bcount[str(c)] += b
    else:
        bcount[str(c)] = b


lc = list(lc)
heapq.heapify(lc)

cnt = 0
ans = 0

while cnt < n:
    amax = -a[0]
    cmax = -1 if len(lc) == 0 else -lc[0]
    if amax >= cmax:
        cnt += 1
        ans += heapq.heappop(a)
    else:
        take = min(n - cnt, bcount[str(cmax)])
        cnt += take
        ans += heapq.heappop(lc) * take

print(-ans)
