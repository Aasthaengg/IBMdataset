x1, x2 = map(int, input().split())
 
l1 = [1,3,5,7,8,10,12]
l2 = [4,6,9,11]
l3 = [2]
 
if (x1 in l1) & (x2 in l1):
  print("Yes")
elif (x1 in l2) & (x2 in l2):
  print("Yes")
elif (x1 in l3) & (x2 in l3):
  print("Yes")
else:
  print("No")