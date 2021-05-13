a, b, c = map(int, input().split())

r = 4*a*b
l = (a+b-c)**2

if r < l and c-a-b > 0:
  print("Yes")
else:
  print("No")