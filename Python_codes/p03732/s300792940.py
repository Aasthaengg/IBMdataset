from itertools import accumulate
n,w=map(int, input().split())
items = {}
for _ in range(n):
    u,v = map(int, input().split())
    if u not in items:
        items[u] = []
    items[u].append(v)
cost = 0
acc = []
minkey = min(items.keys())
for i in range(4):
    if minkey + i in items:
        items[minkey + i].sort(reverse=True)
        acc.append([0] + list(accumulate(items[minkey + i])))
    else:
        acc.append([0])

ans = 0
for i in range(len(acc[0])):
    a = (i) * minkey
    if w < a:
        continue
    for j in range(len(acc[1])):
        b = (j) * (minkey+1)
        if w < a + b:
            continue
        for k in range(len(acc[2])):
            c = (k) * (minkey+2)
            if w < a + b + c:
                continue
            for l in range(len(acc[3])):
                d = (l) * (minkey+3)
                if w < a + b + c + d:
                    continue
                cost = acc[0][i] + acc[1][j] + acc[2][k] + acc[3][l]
                if cost > ans :
                    ans = cost

print(ans)
