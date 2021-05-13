a,b=input().split(" ")
n=int(a+b)
m=n**(1/2)
if m.is_integer():
  print("Yes")
else:
  print("No")