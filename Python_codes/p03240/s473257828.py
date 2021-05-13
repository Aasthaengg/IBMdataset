n = int(input())
dat = []
for _ in range(n):
    a,b,c = map(int,input().split())
    dat.append( [a,b,c] )
can = True

for x in range(101):
    for y in range(101):
        for i in range(n):
            h = None
            can = True
            xx, yy, hh = dat[i]
            h = hh + abs(xx - x) + abs(yy - y)
            for j in range(n):
                xx, yy, hh = dat[j]
                canh = h - abs(xx - x) - abs(yy - y)
                canh = max(canh, 0)
                if canh != hh:
                    can = False
            if can:
                break
        if can:
            break
    if can:
        break
print(x, y, h)