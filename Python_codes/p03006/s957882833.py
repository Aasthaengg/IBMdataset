n = int(input())
dat = []
for i in range(n):
    a,b = map(int, input().split())
    dat.append([a,b])
dat2 = []
if n == 1:
    print(1)
else:
    for i in range(n):
        x1, y1 = dat[i]
        for j in range(n):
            if i == j:
                continue
            x2, y2 = dat[j]
            dat2.append( (x1-x2, y1-y2) )
    import collections
    c = collections.Counter(dat2)
    #print(c)
    ta, tb = c.most_common(1)[0][0]
    res = 0
    for i in range(n):
        canwarp = False
        x1, y1 = dat[i]
        for j in range(n):
            if i == j:
                continue
            x2, y2 = dat[j]
            if x1-x2 == ta and  y1-y2 == tb:
                canwarp = True
        if canwarp:
            continue
        else:
            res += 1
    print(res)
