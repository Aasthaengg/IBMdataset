total = 0
N = input()
for c in N:
  total += int(c)
if total % 9 == 0:
  print("Yes")
else:
  print("No")