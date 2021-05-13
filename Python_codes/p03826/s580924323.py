arr = list(map(int, input().split()))
a = arr[0] * arr[1]
b = arr[2] * arr[3]
if a >= b:
  print(a)
else:
  print(b)