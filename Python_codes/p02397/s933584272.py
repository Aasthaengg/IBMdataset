while 1:
  a = map(int, raw_input().split())
  if a[0]==0 and a[1]==0:
    break
  else:
    a.sort()
    print '%d %d' % (a[0], a[1])