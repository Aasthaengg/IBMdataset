s = input()
x, y = map(int, input().split())

dpx = {0}
dpy = {0}

f = s.split("T")

fx = []
fy = []

for i, fi in enumerate(f):
    if i % 2:
        fy.append(len(fi))
    else:
        fx.append(len(fi))

for i, fxi in enumerate(fx):
    nex = set([])
    for j in dpx:
        nex.add(j+fxi)
        if i > 0:
            nex.add(j-fxi)
    dpx = nex
        
for fyi in fy:
    nex = set([])
    for j in dpy:
        nex.add(j+fyi)
        nex.add(j-fyi)
    dpy = nex

if x in dpx and y in dpy:
    print('Yes')
else:
    print('No')