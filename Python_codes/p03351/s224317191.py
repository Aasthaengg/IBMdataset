a, b, c, d=map(int,input().split())
k1=abs(a-b)
k2=abs(a-c)
k3=abs(b-c)
if k2<=d:
  print("Yes")
elif k1<=d and k3<=d:
  print("Yes")
else:
  print("No")