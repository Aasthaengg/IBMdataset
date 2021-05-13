def solve():
  size = 101
  n = int(input())
  points = []
  for _ in range(n):
    x, y, h = map(int, input().split())
    # h=0の点はスキップ ←勾配がないので高さ計算に使えない
    if h == 0: continue
    else: points.append((x, y, h))

  if len(points) == 1:
    # 必ず頂上が1つに定まる制約なので、測定点が1つしかなければそれが答え
    ans = points[0]
    return ans

  ans = (-1, -1, -1)
  for i in range(size):
    for j in range(size):
      # 高いほうに持ち上げるよう試みて、整合性とれなければ却下
      max_h = None
      succ = True
      for x, y, h in points:
        tmp = abs(i-x) + abs(j-y) + h
        if max_h == None:
          max_h = tmp
          continue
        else:
          if max_h != tmp:
            succ = False
            break
      # 成り立っているなかでの最高点を更新していく
      if succ:
        if ans[2] < max_h:
          ans = (i, j, max_h)
  # すべて終了
  return ans

ans = solve()
print('{} {} {}'.format(ans[0], ans[1], ans[2]))