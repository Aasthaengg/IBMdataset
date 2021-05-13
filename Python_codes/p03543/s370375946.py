n = input()
ok = False
if n[0] == n[1] == n[2]: ok = True
if n[1] == n[2] == n[3]: ok = True
if ok: print('Yes')
else: print('No')