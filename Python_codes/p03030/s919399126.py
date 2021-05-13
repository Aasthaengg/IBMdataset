n = int(input())
d = {}
for i in range(1,n+1):
    s, p = input().split()
    if s in d.keys():
        d[s][i] = int(p)
    else:
        d[s] = {i:int(p)}
for k, v in sorted(d.items()):
    for kk, vv in sorted(v.items(), key=lambda x: -x[1]):
        print(kk)