lis1=[1,3,5,7,8,10,12]
lis2=[4,6,9,11]
lis3=[2]
x,y=map(int,input().split())
if (x in lis1 and y in lis1) or (x in lis2 and y in lis2) or(x in lis3 and y in lis3):
  print("Yes")
else:
  print("No")