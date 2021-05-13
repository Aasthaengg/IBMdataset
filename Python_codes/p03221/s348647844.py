N, M = map(int, input().split())

V = [[] for _ in range(N)]
for i in range(M):
    p, y = map(int, input().split())
    V[p-1].append((y, i))

ans = [0] * M
for i, v in enumerate(V, start=1):
    v.sort()
    for j, (y, k) in enumerate(v, start=1):
        ans[k] = format(str(i), "0>6") + format(str(j), "0>6")

for a in ans:
    print(a)
