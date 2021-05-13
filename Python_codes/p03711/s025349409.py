x,y = map(int,input().split())


a = [1,3,5,7,8,10,12]
b = [4,6,9,11]
c = [2]


if (x in a) & (y in a):
  print("Yes")
elif (x in b) & (y in b):
  print("Yes")
elif (x in c) & (y in c):
  print("Yes")
else:
  print("No")