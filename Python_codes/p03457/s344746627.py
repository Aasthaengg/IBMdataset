N = int(input())
t, x, y = [0]*3
for _ in range(N):
  t_, x_, y_ = map(int, input().split())
  dis = abs(x_ - x) + abs(y_ - y)
  dt = t_ - t
  if dis > dt:
    print("No")
    exit()
  if dis%2 == dt%2:
    t, x, y = t_, x_, y_
  else:
    print("No")
    exit()
print("Yes")