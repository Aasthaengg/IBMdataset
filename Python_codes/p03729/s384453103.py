a,b,c = input().split()
sa = len(a)
sb = len(b)
ok = True
if a[sa-1] != b[0]: ok = False
if b[sb-1] != c[0]: ok = False
if ok: print('YES')
else: print('NO')