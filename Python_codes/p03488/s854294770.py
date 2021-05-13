S = input()
X, Y = map(int, input().split())

if S.find("F") < 0:
    if X != 0 or Y != 0:
        print("No")
    else:
        print("Yes")
    exit()

n = len(S)
d = list(map(len, S.split("T")))
xs = d[::2]
ys = d[1::2]

dpx = [set() for _ in range(len(xs))]
for i in range(len(xs)):
    if i == 0:
        d = (-1) ** S.find("F")
        dpx[i].add(d * xs[i] + n)
        continue
    
    for j in dpx[i - 1]:
        dpx[i].add(j + xs[i])
        dpx[i].add(j - xs[i])

dpy = [set() for _ in range(len(ys) + 1)]
dpy[0].add(n)
for i in range(len(ys)):
    for j in dpy[i]:
        dpy[i + 1].add(j + ys[i])
        dpy[i + 1].add(j - ys[i])

ans = (X + n in dpx[-1]) & (Y + n in dpy[-1])
print("Yes" if ans else "No")
