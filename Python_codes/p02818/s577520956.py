a, b, k = map(int, input().split())
taka = a - k

if taka >= 0:
  print(taka, b)
elif taka < 0:
  aoki = b + taka
  if aoki >= 0:
    print(0, aoki)
  else:
    print(0, 0)
