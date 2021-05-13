x, y = map(int, input().split())

if y % 2 != 0:
  print("No")
  exit()
elif 4 * x < y:
  print("No")
  exit()
elif 2 * x > y:
  print("No")
  exit()

print("Yes")