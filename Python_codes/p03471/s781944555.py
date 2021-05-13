n, y = map(int, input().split())

if n*10000 == y:
  print(n, 0, 0)
elif n*10000 < y:
  print(-1, -1, -1)
else:
  flag = 0
  #sub = n*10000 - y
  for a in range(y//10000+1):
    b_c = n-a
    for b in range(b_c+1):
      c = b_c-b
      if y == a*10000 + b*5000 + c*1000:
        print(a, b, c)
        flag = 1
        break
    if flag == 1:
      break
  if flag == 0:
    print(-1, -1, -1)