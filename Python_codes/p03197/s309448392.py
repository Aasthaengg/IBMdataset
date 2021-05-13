n = int(input())
for i in range(n):
  x = int(input())
  if x%2:
    print("first")
    exit()
else:
  print("second")