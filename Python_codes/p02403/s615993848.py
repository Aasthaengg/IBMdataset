while True:
  H, W = [int(x) for x in input().strip().split(' ')]
  if H == 0 and W == 0:
    break
  for _ in range(H):
    print('#'*W)
  print('')