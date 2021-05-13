s = input()
x, y = map(int, input().split())
x += 8500
y += 8500

dpx = [0 for i in range(17000)]
dpy = [0 for i in range(17000)]

dpx[8500] = 1
dpy[8500] = 1

f = s.split("T")

fx = []
fy = []

for i, fi in enumerate(f):
    if i % 2:
        fy.append(len(fi))
    else:
        fx.append(len(fi))

for i, fxi in enumerate(fx):
    nex = [0] * 17000
    for j in range(17000):
        if dpx[j]:
            if fxi + j < 17000:
                nex[fxi + j] = 1
            if i > 0 and j - fxi >= 0:
                nex[j - fxi] = 1
    dpx = nex
        
for fyi in fy:
    nex = [0] * 17000
    for j in range(17000):
        if dpy[j]:
            if fyi + j < 17000:
                nex[fyi + j] = 1
            if j - fyi >= 0:
                nex[j - fyi] = 1
    dpy = nex

if dpx[x] and dpy[y]:
    print('Yes')
else:
    print('No')
