n, m, x = map(int, input().split())
dat = []
gold = []
for i in range(n):
    l = list(map(int, input().split()))
    gold.append(l[0])
    dat.append(l[1:])
inf = 99999999999999999999
minval = inf
for pat in range(2 ** n):
    tmp = [0] * m
    cost = 0
    for i in range(n):
        if (pat >> i & 1) == 1:
            cost += gold[i]
            for j in range(m):
                tmp[j] += dat[i][j]
    can = True
    for i in range(m):
        if tmp[i] < x:
            can = False
            break
    if can is False:
        continue
    minval = min(minval, cost)

if minval == inf:
    print(-1)
else:
    print(minval)


