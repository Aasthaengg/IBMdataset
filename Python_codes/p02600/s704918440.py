x = int(input())

for i in range(1, 9):
  if 200 + 200 * i <= x <= 399 + 200 * i:
    print(9 - i)