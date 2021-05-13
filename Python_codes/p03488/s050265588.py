s = input()
x, y = map(int, input().split())
l = s.split("T")
#print(l)
x -= len(l[0])
ys = []
xs = []
if len(l) == 1:
  if x == 0 and y == 0:
    print("Yes")
  else:
    print("No")
  exit(0)
for i in range(len(l)):
  if i == 0:
    continue
  if i % 2:
    ys.append(len(l[i]))
  else:
    xs.append(len(l[i]))
#移動しうるマスの総数はなんとか全列挙できるレベル
#先頭からi番目まで見たとき、移動可能であるマス
#何x何のDPなら追いつくのか考える
#bitDPするよりずっと現実的
#集合を使うと無駄なカウントがない
dpx = set()
dpx.add(0)
for i in range(len(xs)):
  nextset = set()
  for j in dpx:
    nextset.add(j + xs[i])
    nextset.add(j - xs[i])
  dpx = nextset
dpy = set()
dpy.add(0)
for i in range(len(ys)):
  nextset = set()
  for j in dpy:
    nextset.add(j + ys[i])
    nextset.add(j - ys[i])
  dpy = nextset
if x in dpx and y in dpy:
  print("Yes")
else:
  print("No")