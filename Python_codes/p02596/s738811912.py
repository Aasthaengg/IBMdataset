K = int(input())

if K % 2 == 0 or K % 5 == 0:
  print(-1)
else:
  if K % 7 == 0:
    L = 9 * K // 7
  else:
    L = 9 * K
  a = 10 % L
  check = False
  for i in range(L):
    a %= L
    if a == 1:
      print(i + 1)
      check = True
      break
    a *= 10
  if not check:
    print(-1)