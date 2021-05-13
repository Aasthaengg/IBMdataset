coin500, coin100, coin50, total = map(int, [int(input()) for i in range(4)])
count = 0;
for i in range(coin500 + 1):
  for j in range(coin100 + 1):
    for z in range(coin50 + 1):
      if 500 * i + 100 * j + 50 * z == total:
        count += 1
print(count)