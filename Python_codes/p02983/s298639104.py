L,R=map(int,input().split())

min_val = 2019
flag = 1
for i in range(L, min(R,L+2019-1), 1):
  for j in range(i+1, min(R+1,L+2019), 1):
    tmp = (i*(j)) % 2019
    if tmp == 0:
      flag = 0
      break
    elif tmp < min_val:
      min_val = tmp
  if flag == 0:
    break
if flag == 0:
  print(0)
else:
  print(min_val)