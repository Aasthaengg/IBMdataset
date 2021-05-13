N = int(input())
now_x, now_y = 0, 0
time = 0
for i in range(N):
  t, x, y = map(int, input().split())
  board = abs(x - now_x) + abs(y - now_y)
  if board > t - time:
    print("No")
    quit()
  elif ((t - time) - board) % 2 == 1:
    print("No")
    quit()
  else:
    now_x, now_y, time = x, y, t
    
print("Yes")




