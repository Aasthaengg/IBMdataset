n = int(input())
count = 0
for i in range(n):
  d1, d2 = map(int, input().split())
  if count > 2:
    break
  else:
    if d1 == d2:
      count += 1
    else:
      count = 0
if count > 2:
  print("Yes")
else:
  print("No")