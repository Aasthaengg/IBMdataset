x,y = map(int,input().split())
a = [1,3,5,7,8,10,12]
b = [4,6,9,11]
c = [2]
if a.count(x)*a.count(y) == 1 or b.count(x)*b.count(y) == 1 or c.count(x)*c.count(y):
  print("Yes")
else:
  print("No")