while True:
  n = int(input())
  if n == 0:
    break

  scr = list(map(int, input().split()))
  avg = sum(scr) / n
  v = 0
  for scri in scr:
    v += ((scri - avg) ** 2 ) / n
  a = v ** 0.5
  print(a)
