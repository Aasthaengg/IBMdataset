n, m = map(int,input().split())

d = {}
for i in range(m):
    p, y = map(int,input().split())
    if p not in d:
        d[p] = [(y, i)]
    else:
        d[p].append((y, i))

ans = [0]*m
for k, v in d.items():
    vl = v
    vl.sort()
    num = 1
    for city in vl:
        pre = str(k).zfill(6)
        c = str(num).zfill(6)
        ans[city[1]] = pre+c
        num += 1
print(*ans,sep="\n")