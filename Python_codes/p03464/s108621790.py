K = int(input())
A = list(map(int, input().split()))

_min=2
_max=2

for a in A[::-1]:
  # min ~ maxでaの倍数 minはそのまま、maxは＋(a-1)
  if _min%a:
    if a*(_min//a) + a > _max:
      print(-1)
      break
    else:
      _min = a*(_min//a) + a
  else:
    _min = _min
  
  _max = a*(_max//a) + a-1
else:
  print(_min, _max)