h, w, d = map(int, input().split())
a = []
for i in range(h):
    a.append(list(map(int, input().split())))
dic=dict()
for i in range(h):
    for j in range(w):
        dic[a[i][j]] = (i, j)
co_order = [None] + [value for key, value in sorted(dic.items(), key=lambda x: x[0])]
cost = {i: [0] for i in range(1, d + 1)}

for i in range(1, d + 1):
    sx, sy= co_order[i]
    for ex, ey in co_order[i+d::d]:
        cost[i].append(cost[i][-1] + abs(sx - ex) + abs(sy - ey))
        sx, sy = ex, ey
q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    index = (r-1)%d+1
    print(cost[index][(r-1)//d] - cost[index][(l-1)//d])