while 1:
  H, W = map(int, raw_input().split())
  s = ""

  if H == 0 and W == 0:
    break

  for i in range(H):
    for j in range(W):
      if i%2 == 0:
        if j%2 == 0:
          s = s + "#"
        else:
          s = s + "."
      else:
        if j%2 == 0:
          s = s + "."
        else:
          s = s + "#"
    print s
    s = ""
  print ""