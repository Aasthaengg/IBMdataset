a1 = [1,3,5,7,8,10,12]
a2 = [4,6,9,11]
a3 = [2]

x,y = list(map(int,input().strip().split()))

if x in a1:
  _x = 0
elif x in a2:
  _x = 1
else:
  _x = 2
  
if y in a1:
  _y = 0
elif y in a2:
  _y = 1
else:
  _y = 2
  
if _x == _y:
  print("Yes")
else:
  print("No")