a,b,c,d,e,f = map(int, input().split())
ws = []
for i in range(f//100//a+1):
    for j in range(f//100//b+1):
        w = 100*(a*i+b*j)
        if 0 < w <= f:
            ws.append(w)
        if w >= f:
            break
ss = []
for i in range(f*e//(100+e)//c+1):
    for j in range(f*e//(100+e)//d+1):
        s = c*i+d*j
        if 0 <= s <= f*e//(100+e):
            ss.append(s)
n = []
for w in ws:
    for s in ss:
        if w+s > f:
            continue
        if s > e*w//100:
            continue
        n.append((s/(w+s), w+s, s))

nmax = max(n, key=lambda x:x[0])
print(nmax[1], nmax[2])
