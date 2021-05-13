from copy import copy
Ss = input() + "T"
X, Y = map(int, input().split())

d = [len(s) for s in Ss.split("T")]
x = d[0]
# x,y方向に分解
d_x = d[2::2]
d_y = d[1::2]

xs = set([x])
ys = set([0])
blx = [X in xs]
for d in d_x:
    # 各移動後に、X座標にいるかcheck
    xs_ = set()
    for x in xs:
        xs_.add(x+d)
        xs_.add(x-d)
    blx.append(X in xs_)
    xs = copy(xs_)

bly = []
for d in d_y:
    ys_ = set()
    for y in ys:
        ys_.add(y+d)
        ys_.add(y-d)
    bly.append(Y in ys_)
    ys = copy(ys_)

if blx[-1] and bly[-1]: print("Yes")
else: print("No")