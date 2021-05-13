n, m = map(int, input().split())

dic = dict()
for i in range(m):
    p, y = map(int, input().split())
    if not p in dic:
        dic[p] = []
    dic[p].append((y, i+1))

ans = []
for p, l in dic.items():
    l.sort()
    for i, x in enumerate(l):
        ans.append([x[1], str(p).zfill(6) + str(i + 1).zfill(6)])
ans.sort()

for x in ans:
    print(x[1])