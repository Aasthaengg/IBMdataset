while True:
  h, w = [int(n) for n in input().split()]
  if h == 0 and w == 0:
    quit()

  for i in range(0, h):
    for j in range(0, w):
      print("#", end='')
    print()
  print()