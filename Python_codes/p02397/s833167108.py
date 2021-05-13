while 1:
  x, y = map(int, raw_input().split())
  if x == 0 and y == 0:
    break
  else:
    if x > y:
      temp = x
      x = y
      y = temp
  print '{0} {1}'.format(x, y)