a, b, c = list(map(int, input().split()))
if a == b == c:
  print(1)
else:
  if a == b or b == c or c == a:
    print(2)
  else:
    print(3)