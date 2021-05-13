X = int(input())

more_100 = X/100
under_100 = X%100
X2 = int(under_100 / 5)
X3 = under_100 % 5
if X3 != 0 and X2 + 1 <= more_100:
  print(1)
elif X3 == 0 and X2 <= more_100:
  print(1)
else:
  print(0)