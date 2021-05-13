l = [1,3,5,7,8,10,12]
m = [4,6,9,11]
a,b  = map(int,input().split())
if (a in l and b in l) or (a in m and b in m):
  print("Yes")
else:
  print("No")