s = input()
n = len(s)
x, y = map(int, input().split())
for i in range(n):
    if s[i]=='T':
        break
else:
    i += 1
dp = {i}
xs = []
ys = []
now = 0
xy = 'y'
for j in range(i+1, n+1):
    if j<n and s[j]=='F':
        now += 1
        continue
    if xy=='x':
        if now>0:
            xs.append(now)
        xy = 'y'
    else:
        if now>0:
            ys.append(now)
        xy = 'x'
    now = 0

for i in xs:
    newdp = set()
    for j in dp:
        newdp.add(j+i)
        newdp.add(j-i)
    dp = newdp
if x not in dp:
    print('No')
    exit(0)
dp = {0}
for i in ys:
    newdp = set()
    for j in dp:
        newdp.add(j+i)
        newdp.add(j-i)
    dp = newdp
if y in dp:
    print('Yes')
else:
    print('No')