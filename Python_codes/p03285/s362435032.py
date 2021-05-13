N = int(input())
flag = False
for i in range(101):
  if 4*i > N:
    break
  else:
    a = (N -i*4) % 7
    if a == 0:
      flag = True
      break
if flag:
  print("Yes")
else:
  print("No")