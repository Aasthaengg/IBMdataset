N = int(input())
a = 25-N
res = "Christmas"
if a == 0:
  print(res)
else:
  for i in range(a):
    res += " Eve"
  print(res)