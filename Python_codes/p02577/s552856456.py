n = int(input())

SUM = sum(list(map(int, str(n))))

if SUM % 9 == 0:
  print("Yes")
else:
  print("No")