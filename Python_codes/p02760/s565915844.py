b = []
for i in range(3):
  lst = list(map(int,input().split()))
  b.append(lst)
n = int(input())
for i in range(n):
  a = int(input())
  for j in range(3):
    for k in range(3):
      if (b[j][k] == a):
        b[j][k] = 0
if (b[0][0] == b[0][1] == b[0][2] or b[1][0] == b[1][1] == b[1][2] or b[2][0] == b[2][1] == b[2][2] or b[0][0] == b[1][0] == b[2][0] or b[0][1] == b[1][1] == b[2][1] or b[0][2] == b[1][2] == b[2][2] or b[0][0] == b[1][1] == b[2][2] or b[0][2] == b[1][1] == b[2][0]):
  print("Yes")
else:
  print("No")
  
