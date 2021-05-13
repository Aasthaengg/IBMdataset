from collections import defaultdict

N, M = map(int, input().split())
*l, = [tuple(map(int, input().split())) for _ in range(M)]
ans = M

for i in range(M):
    d = defaultdict(list)
    for j in range(M):
        if j==i:continue
        a, b = l[j]
        d[a].append(b)
        d[b].append(a)
    q = [a]
    used = [False]*(N+1)
    used[0] = True
    used[a] = True
    while q:
        s = q.pop()
        for t in d[s]:
            if used[t]:continue
            used[t] = True
            q.append(t)
    if all(used):
        ans -= 1
print(ans)
