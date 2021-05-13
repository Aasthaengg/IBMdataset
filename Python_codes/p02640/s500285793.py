a, b = map(int, input().split())
if b%2 != 0:
  print("No")
elif 2*a <= b and b <= 4*a:
  print("Yes")
else:
  print("No")