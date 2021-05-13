a,b,c = map(int, input().split())
if a-b == 0:
  print(c)
elif a-c == 0:
  print(b)
else:
  print(a)