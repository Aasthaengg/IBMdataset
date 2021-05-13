X = int(input())
if X >= 400 and X <= 599:
  rank = 8
elif X >= 600 and X <= 799:
  rank = 7
elif X >= 800 and X <= 999:
  rank = 6
elif X >= 1000 and X <= 1199:
  rank = 5
elif X >= 1200 and X <= 1399:
  rank = 4
elif X >= 1400 and X <= 1599:
  rank = 3
elif X >= 1600 and X <= 1799:
  rank = 2
elif X >= 1800 and X <= 1999:
  rank = 1
print(rank)