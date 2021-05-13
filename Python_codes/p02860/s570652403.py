n=int(input())
str=input()
before=str[0:int(0.5*n)]
after=str[int(0.5*n):]
if before==after:
  print("Yes")
else:
  print("No")