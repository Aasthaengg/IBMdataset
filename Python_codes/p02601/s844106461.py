A, B, C = map(int, input().split())
K = int(input())
flag = False
for i in range(K+1):
  for j in range(K+1):
    for k in range(K+1):
      x = A * (1 << i)
      y = B * (1 << j)
      z = C * (1 << k)
      if i + j + k <=K and x < y and y < z:
        flag = True

if flag == True:
  print("Yes")
else:
  print("No")

