n = int(input())
flag = True
for i in range(n):
  if int(input()) % 2 == 1:
    flag = False
if flag == True:
  print("second")
else:
  print("first")