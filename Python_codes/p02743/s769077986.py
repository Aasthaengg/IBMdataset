a,b,c = map(int,input().split())
right = (a+b-c)**2
left = 4*a*b
if right > left and c-a-b > 0:
  print("Yes")
else:
  print("No")