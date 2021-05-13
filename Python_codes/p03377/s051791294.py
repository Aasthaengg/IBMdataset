def output(ok):
    if ok: print('YES')
    else: print('NO')
a,b,c = map(int,input().split())
ok = True
if a+b < c: ok = False
elif a > c: ok = False
else:
    c -= a
    if c > b: ok = False
output(ok)