a,b,c=map(int,input().split())
Flag = 0
if a + b == c:
  Flag =1
elif a+c==b:
  Flag = 1
elif b+c==a:
  Flag =1
if Flag == 1:
  print("Yes")
else:
  print("No")