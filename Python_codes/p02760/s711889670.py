a = [0]*3
for i in range(3):
  a[i] = list(map(int, input().split()))
n = int(input())
b = [0]*n
for i in range(n):
  b[i] = int(input())

  
  

  
  
for i in range(n):
  for j in range(3):
    for k in range(3):
      if a[j][k] == b[i]:
        a[j][k] = 0


for i in range(3):
  if sum(a[i]) == 0:
    print("Yes")
    exit()
    
for i in range(3):
  if a[0][i] + a[1][i] + a[2][i] == 0:
    print("Yes")
    exit()
if a[0][0] + a[1][1] + a[2][2] == 0:
  print("Yes")
  exit()
if a[0][2] + a[1][1] + a[2][0] == 0:
  print("Yes")
  exit()
print("No")
