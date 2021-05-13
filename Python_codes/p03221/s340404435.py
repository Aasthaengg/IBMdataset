n, m = map(int, input().split())
pyo = []
for i in range(m):
    p, y = map(int, input().split())
    pyo.append([p, y, i])

sortpy = sorted(pyo, key=lambda x:x[1])

yy = [0]*(n+1)
ans = [""]*m
for i, j, k in sortpy:
    pp = str(i).zfill(6)
    yy[i] += 1
    ans[k] = pp + str(yy[i]).zfill(6)

for i in range(m):
    print(ans[i])