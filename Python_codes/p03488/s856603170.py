s = input()
x, y = map(int,input().split())

s = s.split("T")
s = [len(e) for e in s]
a = []
b = []
for i, s in enumerate(s):
    if i % 2 == 0:
        a.append(s)
    else:
        b.append(s)

x -= a.pop(0)
ans = True

dpx = [[False] * (2*abs(x) + 1) for _ in range(len(a) + 1)]
dpx[0][abs(x)] = True

for i in range(1,len(a)+1):
    for j in range(2*abs(x) + 1):
        if j + a[i-1] < 2*abs(x) + 1:
            dpx[i][j] |= dpx[i-1][j+a[i-1]]
        if j - a[i-1] >= 0:
            dpx[i][j] |= dpx[i-1][j-a[i-1]]

ans &= dpx[len(a)][x+abs(x)]

dpy = [[False] * (2*abs(y) + 1) for _ in range(len(b) + 1)]
dpy[0][abs(y)] = True

for i in range(1, len(b) + 1):
    for j in range(2*abs(y) + 1):
        if j + b[i-1] < 2*abs(y) + 1:
            dpy[i][j] |= dpy[i-1][j+b[i-1]]
        if j - b[i-1] >= 0:
            dpy[i][j] |= dpy[i-1][j-b[i-1]]

ans &= dpy[len(b)][y+abs(y)]

if ans:
    print("Yes")
else:
    print("No")