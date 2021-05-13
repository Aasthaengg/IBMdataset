m,k = map(int,input().split())

if m == 0:
    if k == 0:
        print(0,0)
    else:
        print(-1)
    exit()
if m == 1:
    if k == 0:
        print(0,0,1,1)
    else:
        print(-1)
    exit()
if k >= 2**m:
    print(-1)
    exit()
if k == 0:
    for i in range(2**m):
        print(i,i,end = ' ')
    exit()
res = []
used = [True]*(2**m)

tank = []

for i in range(2**m):
    if used[i]:
        tank.append((i,i^k))
        used[i] = used[i^k] = False
for i in range(len(tank)):
    if i % 2 == 1:
        continue
    a = tank[i][0]
    b = tank[i][1]
    c = tank[i+1][0]
    d = tank[i+1][1]
    res += [c,a,b,c,d,b,a,d]

for e in res:
    print(e,end=' ')
