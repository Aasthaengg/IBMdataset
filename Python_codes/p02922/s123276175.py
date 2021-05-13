a,b = map(int, input().split())
count = 1
if b == 1:
  print(0)
else:
  while True:
    if b <= (a-1)*(count-1) + a:
      break
    count += 1
  print(count)