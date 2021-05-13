x,y=map(int,input().split())
d=[1,3,5,7,8,10,12]
if x==2 or y==2:
  print("No")
elif x in d and y in d:
  print("Yes")
elif x not in d and y not in d:
  print("Yes")
else:
  print("No")