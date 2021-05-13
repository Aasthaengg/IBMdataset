f_1 = {1,3,5,7,8,10,12}
f_2 = {4,6,9,11}
 
x, y = map(int, input().split())
if (x in f_1) and (y in f_1):
  print("Yes")
elif (x in f_2) and (y in f_2):
  print("Yes")
else:
  print("No")