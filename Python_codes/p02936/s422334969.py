from collections import defaultdict

N, Q = map(int, input().split())
d = defaultdict(list)
for _ in range(N-1):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)
ans = [0]*(N+1)
for _ in range(Q):
    p, x = map(int, input().split())
    ans[p] += x

q = [1]
used = [False]*(N+1)
used[1] = True
while q:
    s = q.pop()
    for t in d[s]:
        if used[t]:continue
        used[t] = True
        ans[t]+=ans[s]
        q.append(t)

print(*ans[1:])