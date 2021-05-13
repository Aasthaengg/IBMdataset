n = input()
total = 0
for digit in n:
  total += int(digit)
if total == 1:
  print(10)
else:
  print(total)