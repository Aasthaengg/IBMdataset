x,y = (int(x) for x in input().split())
l1 = [1,3,5,7,8,10,12]
l2 = [4,6,9,11]
l3 = [2]
n = 0
if x in l1:
  if y in l1:
    print ('Yes')
    n = 1
elif x in l2:
  if y in l2:
    print ('Yes')
    n = 1
else:
  if y in l3:
    print ('Yes')
    n = 1
if n == 0:
  print ('No')