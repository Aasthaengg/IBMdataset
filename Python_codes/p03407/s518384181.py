coin_1, coin_2, value = map(int, input().split(' '))
if (coin_1 + coin_2) >= value:
  print("Yes")
else:
  print("No")