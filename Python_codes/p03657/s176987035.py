a, b = map(int, input().split())
if a + b != 0 and (a + b) % 3 == 0:
  print("Possible")
elif a != 0 and a % 3 == 0:
  print("Possible")
elif b != 0 and b % 3 == 0:
  print("Possible")
else:
  print("Impossible")