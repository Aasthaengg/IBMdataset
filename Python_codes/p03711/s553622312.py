a,b=[str(i) for i in input().split()]
list1=["1","3","5","7","8","10","12"]
list2=["4","6","9","11"]
if a in list1 and b in list1:
  print('Yes')
elif a in list2 and b in list2:
  print('Yes')
else:
  print('No')