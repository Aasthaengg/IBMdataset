from copy import copy
s = input() + "T"
x,y = map(int, input().split())

d = [len(p) for p in s.split("T")]
init = d[0]
d_x = d[2::2]
d_y = d[1::2]

xs = set([init])
ys = set([0])
dpx = [x in xs]
for d in d_x:
  xs_ = set()
  for u in xs:
    xs_.add(u+d)
    xs_.add(u-d)
  dpx.append(x in xs_)
  xs = copy(xs_)

dpy = []
for d in d_y:
  ys_ = set()
  for v in ys:
    ys_.add(v+d)
    ys_.add(v-d)
  dpy.append(y in ys_)
  ys = copy(ys_)

if dpx[-1] and dpy[-1]: print("Yes")
else: print("No")