from heapq import heappop, heappush
n, k = map(int, input().split())
lst = [list(map(int, input().split())) for i in range(n)]
lst = sorted(lst, reverse=True, key=lambda x:x[1])
q = []
v = set()
cnt = 0
for t, d in lst[:k]:
    cnt += d
    if t in v:
        heappush(q, d)
    else:
        v.add(t)
cnt += len(v)**2
ans = cnt
for t, d in lst[k:]:
    if t not in v and len(q)!=0:
        x = heappop(q)
        cnt += d + 2*len(v) + 1 - x
        v.add(t)
        ans = max(ans, cnt)
print(ans)