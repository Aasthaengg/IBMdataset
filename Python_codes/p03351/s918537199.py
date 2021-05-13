n = [int(i) for i in input().split()]
flag = False
if(abs(n[0]-n[2]) <= n[3]):
  flag = True
elif(abs(n[0]-n[1]) <= n[3] and abs(n[1]-n[2]) <= n[3]):
  flag = True
if(flag == True):
  print("Yes")
else:
  print("No")