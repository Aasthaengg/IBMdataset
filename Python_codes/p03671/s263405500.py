a, b, c = map(int, input().split())
if a<=b<=c or b<=a<=c:
  print(a + b)
elif a<=c<=b or c<=a<=b:
  print(a + c)
else:
  print(b + c)