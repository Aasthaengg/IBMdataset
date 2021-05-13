a,b,c,d = map(int,input().split())
ok = False
dist = abs(a-c)
if dist <= d: ok = True
else:
    d1 = abs(a-b)
    d2 = abs(b-c)
    if d1 <= d and d2 <= d: ok = True
if ok: print('Yes')
else: print('No')