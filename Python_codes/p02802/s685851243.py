N,M = map(int, input().split())
r = {}
a = {}
for i in range(M):
    l = input().split()
    p = int(l[0])
    q = l[1]
    w = q + str(p)
    if r.get(p) == 'AC':
        pass
    else:
        r.update([(p, q)])
        if a.get(w) != None:
            a[w] += 1
        else:
            a.update([(w, 1)])
ks = [k for k, v in r.items() if v == 'AC']
wa = 0
ac = 0
for i in ks:
    wk = 'WA' + str(i)
    ak = 'AC' + str(i)
    if a.get(wk) != None:
        wa += a[wk]
    ac += a[ak]
print(ac, wa)