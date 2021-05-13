a,b,c = map(int, input().split())
if b >= a*c:
  print(c)
elif b < a*c:
  print(b//a)