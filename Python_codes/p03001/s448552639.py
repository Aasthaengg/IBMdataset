from decimal import Decimal
W, H, x, y = map(int, input().split())
Wi = W * 10 ** 9
Hi = H * 10 ** 9
men = Decimal(W * H / 2)
judge = 0
if x == W / 2 and y == H / 2:
  judge = 1
print("{0:.10f} {1:.0f}".format(men, judge))