import math
a, b, x = map(int, input().split())


if x > a*a*b/2:
  ｘ = x /(a*a)*2
  ok = 0
  ng = 90
  while ng-ok > 10**(-7):
    y = (ok + ng) /2
    if x/2 + a*math.tan(math.radians(y))/2 > b:
      ng = y
    else:
      ok = y
  print(ng)
else:
  x = x/a
  ok = 0
  ng = 90
  while ng-ok > 10**(-7):
    y = (ok + ng) /2
    if x*2/b * math.tan(math.radians(y)) > b:
      ng = y
    else:
      ok = y
  print(ng)
