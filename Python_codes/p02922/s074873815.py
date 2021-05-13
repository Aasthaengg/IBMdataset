a,b = map(int,input().split())

if b == 1:
  print(0)
else:
  num = 1
  while True:
    if a * num - (num-1) >= b:
      break

    num += 1

  print(num)