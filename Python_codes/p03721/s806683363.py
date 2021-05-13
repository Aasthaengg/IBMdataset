n,k = map(int,input().split())
d = {}
for _ in range(n):
    a,b = map(int,input().split())
    if not a in d:
        d[a] = b
    else:
        d[a] += b

c = 0
for v in sorted(d.items()):
    c += v[1]
    if k <= c:
        print (v[0])
        exit ()
