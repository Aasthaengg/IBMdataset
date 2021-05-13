a, b = map(str, input().split())
n = int(a+b)
if (n ** .5).is_integer():
  print("Yes")
else:
  print("No")