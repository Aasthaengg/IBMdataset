n = int(input())
txy = [0]*n

for i in range(n):
  txy[i] = list(map(int,input().split()))

t_ = 0
x_ = 0
y_ = 0

for i in range(n):
  dx = 0
  dy = 0
  t = txy[i][0]
  x = txy[i][1]
  y = txy[i][2]
  dx = abs(x-x_)
  dy = abs(y-y_)
  d = dx + dy
  if d == abs(t - t_):
    t_ = t
    x_ = x
    y_ = y
  elif d > abs(t - t_):
    print("No")
    exit()
  else:
    if (abs(t - t_)-d)%2 == 0:
      t_ = t
      x_ = x
      y_ = y      
    else:
      print("No")
      exit()
      
print("Yes")