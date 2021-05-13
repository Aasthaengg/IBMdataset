n,m=map(int,input().split())
a=(1,3,5,7,8,10,12)
b=(4,6,9,11)
c=(2,)
if n in a and m in a:
  print("Yes")
elif n in b and m in b:
  print("Yes")
elif n in c and m in c:
  print("Yes")
else:
  print("No")