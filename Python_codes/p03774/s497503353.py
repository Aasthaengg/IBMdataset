n, m = map(int, input().split())
ab = []
for i in range(n):
    ai, bi = map(int, input().split())
    ab.append([ai, bi])
cd = []
for i in range(m):
    ci, di = map(int, input().split())
    cd.append([ci, di])

ans = []
for i in range(n):
    ai, bi = ab[i]
    mini = 10**10
    for j in range(m):
        cj, dj = cd[j]
        dist = abs(ai-cj) + abs(bi-dj)
        if dist < mini:
            mini = dist
            ret = j+1
    ans.append(ret)

for ret in ans:
    print(ret)