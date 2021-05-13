while 1:
  x = map(int, raw_input().split())
  if x[0] == 0 and x[1] == 0:
    break
  x.sort()
  print "%d %d" % (x[0], x[1])