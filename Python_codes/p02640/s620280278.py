x, y = map(int,input().split())
f = False
for i in range(x+1):
    if 2*i + 4*(x-i) == y:
        f = True
        break
if f:
    print('Yes')
else:
    print('No')