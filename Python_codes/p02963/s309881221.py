S = int(input())

x1 = 0
y1 = 0
x2 = 10 ** 9
y2 = 1

y3_, x3_  =  divmod(S, x2)
if y3_ == 10 ** 9:
  y3 = y3_
  x3 = x3_
else:
  y3 = y3_ + 1
  x3 = 10 ** 9 - x3_

print(x1, y1, x2, y2, x3, y3)