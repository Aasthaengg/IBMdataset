N = int(input())
l = [list(map(int, input().split())) for i in range(N)]
t, x, y = 0, 0, 0
 
for i in range(N):
  if l[i][0]-t >= abs(l[i][1]-x)+abs(l[i][2]-y) and (l[i][0]-t-abs(l[i][1]-x)+abs(l[i][2]-y)) % 2 == 0:
      t, x, y = l[i][0], l[i][1], l[i][2]
  else:
    print("No")
    break
else:
  print("Yes")