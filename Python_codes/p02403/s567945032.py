while True:
  H, W = map(int, raw_input().split())
  if H == 0 and W == 0:
      break
  print (("#" * W + "\n") * H)