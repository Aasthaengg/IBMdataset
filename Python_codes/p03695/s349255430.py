n = int(input())
a = list(map(int,input().split()))
color = [0,0,0,0,0,0,0,0,0]
if min(a) >= 3200:
  print(1,len(a))
  quit()
for ai in a:
  if ai <= 3199:
    rnk = ai // 400
    color[rnk] += 1
  else:
    color[8] += 1

min_color = 0
for i in range(8):
  if color[i] > 0:
    min_color += 1
max_color = min_color + color[8]
print(min_color,max_color)