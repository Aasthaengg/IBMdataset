def f(start, goal, steps):
  res = set([start])
  for s in steps:
    next_res = set()
    for r in res:
      next_res.add(r + s)
      next_res.add(r - s)
    res = next_res
  return goal in res

s = input()
x, y = map(int, input().split())

ss = s.split("T")
xmove = [i.count("F") for i in ss[::2]]
xfirst = xmove[0] # xの１回目はプラス方向固定のため切り出す
xmove = xmove[1:] # ２回目以降でリスト再作成
ymove = [i.count("F") for i in ss[1::2]]

if f(xfirst, x, xmove) and f(0, y, ymove):
  print("Yes")
else:
  print("No")