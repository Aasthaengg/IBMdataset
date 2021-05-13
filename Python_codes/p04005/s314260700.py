a, b, c = map(int, input().split())
if (a*b*c)%2==0:
  print(0)
else:
  test1 = a*b
  test2 = a*c
  test3 = b*c
  print(min(test1, test3, test2))