import sys

stdin = sys.stdin

ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split()))  # applies to numbers only
rs = lambda: stdin.readline().rstrip()  # ignores trailing space

S = list(rs())
X, Y = rl()

xy = [[], []]
dir = 0 # x軸方向を0とし、y軸方向を1とする
cur = 0
for s in S:
    if s == 'F':
        cur += 1
    else:
        xy[dir].append(cur)
        cur = 0
        dir = 1 - dir
xy[dir].append(cur)
# x軸方向が達成可能かどうか
xmax = sum(xy[0])
dif_x = xmax - X
ymax = sum(xy[1])
dif_y = ymax - Y
if dif_x&1 == 1 or dif_y&1 == 1:
    print('No')
    exit()
dif_x //= 2
dif_y //= 2
xset = set([0])
for x in xy[0][1:]:
    new_set = set()
    for z in xset:
        new_set.add(z+x)
    xset = xset.union(new_set)
yset = set([0])
for y in xy[1]:
    new_set = set()
    for z in yset:
        new_set.add(z+y)
    yset = yset.union(new_set)

if dif_x in xset and dif_y in yset:
    print('Yes')
else:
    print('No')
# 31