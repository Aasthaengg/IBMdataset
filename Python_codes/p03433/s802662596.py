n=int(input())
a=int(input())
x=n-(n//500)*500
if x>a:
  print("No")
else:
  print("Yes")