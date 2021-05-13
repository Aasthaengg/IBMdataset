while True:
  h, w = [int(n) for n in input().split()]

  if h == 0 and w == 0:
    quit()

  for i in range(0, h):
    for j in range(0, w):
      if i%2 == 0 and j%2 == 1 or i%2 == 1 and j%2 == 0:
        print(".", end='')
      else:
        print("#", end='')
    print()
  print()