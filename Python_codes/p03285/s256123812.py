n = int(input())
a = n//4 # max x
b = n//7 # max y
ok = False
for x in range(0,a+1):
    for y in range(0,b+1):
        if n == 4*x + 7*y:
            ok = True
            break
    if ok: break

if ok: print('Yes')
else: print('No')
