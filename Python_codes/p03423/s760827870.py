a=int(input())
if a<3:
  print(0)
elif a%3==0:
  print(a//3)
elif a%3==1:
  print((a-1)//3)
else:
  print((a-2)//3)