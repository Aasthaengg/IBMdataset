a =  list(map(int, input().split()))

b = a[2] + a[1] - a[0]

if b <= 0:
  print(0)
else:
  print(b)