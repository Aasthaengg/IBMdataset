N, M = map(int, input().split())
piys = [[] for _ in range(N)]
for i in range(M):
    p, y = map(int, input().split())
    piys[p-1].append((y, i))

ans = [None]*M
for p, iys in enumerate(piys):
    iys.sort()
    for k, (y, i) in enumerate(iys):
        ans[i] = "%06d%06d" % (p+1, k+1)

for i in ans:
    print(i)