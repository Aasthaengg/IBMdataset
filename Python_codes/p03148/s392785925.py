N, K = map(int, input().split())
td = [list(map(int, input().split()))
      for _ in range(N)]
td.sort(key=lambda x: -x[1])
q = []
v = set()
cnt = 0
for t, d in td[:K]:
    cnt += d
    if t in v:
        q.append(d)
    else:
        v.add(t)
cnt += len(v) ** 2
ans = cnt
for t, d in td[K:]:
    if t not in v and len(q) != 0:
        x = q.pop()
        cnt += d + 2 * len(v) + 1 - x
        v.add(t)
        ans = max(ans, cnt)
print(ans)
