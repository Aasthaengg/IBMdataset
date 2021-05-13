x,y=map(int,input().split())
a={1,3,5,7,8,10,12}
b={4,6,9,11}
c={2}
if x in a:
  group_x=0
elif x in b:
  group_x=1
else:
  group_x=2

if y in a:
  group_y=0
elif y in b:
  group_y=1
else:
  group_y=2

if group_x==group_y:
  print("Yes")
else:
  print("No")
