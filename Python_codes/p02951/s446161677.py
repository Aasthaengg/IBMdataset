#--Transfer

a, b, c = map(int, input().split())

judge = a - (b + c)
if (judge <= 0):
  print(-judge)
else:
  print("0")
