n, m = map(int, input().split())
d = [[] for _ in range(n)]
ans = [[] for _ in range(m)]
for i, _ in enumerate(range(m)):
    p, y = map(int, input().split())
    d[p-1].append([i, y])
for i in range(n):
    d[i].sort(key=lambda x:x[1])
    for j in range(len(d[i])):
        ans[d[i][j][0]].append(str(i+1).zfill(6)+str(j+1).zfill(6))
for i in ans: print(*i)