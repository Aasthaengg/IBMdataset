w, h, n = map(int, input().split())

s = [list(map(int, input().split())) for i in range(n)]

min_x = 0
max_x = w
min_y = 0
max_y = h

for i in range(n):
  if s[i][2] == 1:
    if s[i][0] > min_x:
      min_x = s[i][0]

  elif s[i][2] == 2:
    if s[i][0] < max_x:
      max_x = s[i][0]
      
  elif s[i][2] == 3:
    if s[i][1] > min_y:
      min_y = s[i][1]
      
  else:
    if s[i][1] < max_y:
      max_y = s[i][1]

if (max_x - min_x) > 0 and (max_y - min_y) > 0:
  print((max_x - min_x) * (max_y - min_y))
  
else:
  print(0)
