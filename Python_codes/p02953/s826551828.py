n = int(input())
h = list(map(int,input().split()))

cmax = h[0]
ok = True
for i in h:
    cmax=max(cmax,i)
    if cmax-i>1:
        ok = False
        break
        
if ok:
    print('Yes')
else:
    print('No')