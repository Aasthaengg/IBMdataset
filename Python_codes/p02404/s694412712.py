while True:
  H, W = map(int, raw_input().split())
  if H == 0 and W == 0:
    break
  print "#"*W
  for i in range(H-2):
    if W > 2:
      print "#" + "."*(W-2) + "#"
    else:
      print "#"*W 
  print "#"*W
  print ""