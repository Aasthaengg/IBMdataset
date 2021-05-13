n,k = map(int,input().split())
d= {}
for i in range(n):
    a,b=map(int, input().split())
    if d.get(a):
        d[a] +=b
    else:
        d[a] = b
res = 0
for key in sorted(d.keys()):
    if d[key]+res>=k:
        print(key)
        exit()
    res += d[key]