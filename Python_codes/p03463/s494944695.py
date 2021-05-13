n,a,b = map(int,input().split())
cnt = 1
while True:
  if cnt % 2 != 0: #alice
    cnt += 1
    a += 1
    if a == b:
      print('Borys')
      break
  else:
    cnt += 1
    b -= 1
    if b == a:
      print('Alice')
      break