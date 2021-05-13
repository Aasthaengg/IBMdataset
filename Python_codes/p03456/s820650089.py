a,b = input().split()
a += b
can = 0
for i in range(1,1000):
  if(i*i == int(a)):
    can = 1
if(can == 1):
  print("Yes")
else:
  print("No")