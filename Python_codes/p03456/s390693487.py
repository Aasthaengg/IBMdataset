a,b=input().split()
c=a+b
c=int(c)
i=0
while i**2<=c:
  i=i+1
if (i-1)**2==c:
  print("Yes")
else:
  print("No")