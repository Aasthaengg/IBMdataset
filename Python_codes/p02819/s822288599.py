X = int(input())
if X == 2:
  print(X)
while X > 2:
  if X % 2 == 0:
    # 偶数
    X += 1
  else:
    n = 3
    while n * n <= X:
      if X % n == 0:
        # 割り切れる
        X += 1
        break
      n += 1
    else:
      print(X)
      break