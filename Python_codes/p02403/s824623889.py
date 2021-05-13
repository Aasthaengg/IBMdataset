while True:
  a, b = map(int, input().split())
  if a == b == 0:
    break

  for i in range(0,a):
    print('#' * b)

  print()
