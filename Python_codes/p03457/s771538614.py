n=int(input())
old_t = 0
old_x = 0
old_y = 0
for i in range(n):
  t, x, y = map(int, input().split())
  if (t - old_t) < abs(x-old_x)+abs(y-old_y) or (t - old_t)%2 != (abs(x-old_x)+abs(y-old_y))%2:
    print("No")
    break
  old_t, old_x, old_y = t, x, y
else:
  print("Yes")
