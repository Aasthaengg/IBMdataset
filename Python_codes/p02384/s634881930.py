ns=tuple(map(int,input().split()))

def rot(d, r):
    if r == 'N':
        return (d[1], d[5], d[2], d[3], d[0], d[4])
    if r == 'E':
        return (d[3], d[1], d[0], d[5], d[4], d[2])
    if r == 'W':
        return (d[2], d[1], d[5], d[0], d[4], d[3])
    if r == 'S':
        return (d[4], d[0], d[2], d[3], d[5], d[1])
    return d

ds = { ns }

while 1:
    d2 = { rot(d, r) for d in ds for r in list('NEWS') }.union(ds)
    if ds == d2: break
    ds = d2

q=int(input())
for _ in range(q):
    qs=list(map(int,input().split()))
    print([ d for d in ds if d[0] == qs[0] and d[1] == qs[1] ][0][2])