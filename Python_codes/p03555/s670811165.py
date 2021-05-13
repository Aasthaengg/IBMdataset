x = input()
y = input()

x = list(x)
y = list(y)
x_ = x
y_ = y
x_ = reversed(x)
y_ = reversed(y)
x_ = list(x_)
y_ = list(y_)


if y_ == x and x_ == y:
  print("YES")
else:
  print("NO")