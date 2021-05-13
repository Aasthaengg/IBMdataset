x = int(input())
flag = False
for i in range(26):
  left = x-4*i
  if left>=0 and left%7==0:
    flag=True
    break
if flag:
  print("Yes")
else:
  print("No")