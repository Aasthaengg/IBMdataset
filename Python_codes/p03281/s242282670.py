N = int(input())

if N < 105:
  print(0)
else:
  ans = 0
  for i in range(105, N + 1, 1):
    y = 0
    for j in range(1, i + 1, 1):
      if i % 2 == 0:
        break
      else:
        if i % j == 0:
          y += 1
    else:
      if y == 8:
        ans += 1
  else:
    print(ans)

