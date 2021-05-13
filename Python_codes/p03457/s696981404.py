n = int(input())
a = [[0, 0, 0]]
for _ in range(n):
  a.append(list(map(int, input().split())))

flag = 0
for i in range(n):
  delta = a[i+1][0]-a[i][0]
  distance = abs(a[i+1][1]-a[i][1]) + abs(a[i+1][2]-a[i][2])
  if delta < distance or delta%2 != distance%2:
    flag = 1
    break
    
if flag == 1:
  print("No")
else:
  print("Yes")