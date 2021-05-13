x = int(input())
x11 = x/11
num = [1,2,3,4,5,6]
num2= [7,8,9,10]

if x in num:
  print(1)
  exit()
elif x in num2:
  print(2)
  exit()

elif int(x11) == x11:
  print(int(x11)*2)
  exit()
elif x > int(x11)*11 + 6:
  print(int(x11)*2 +2)
  exit()
else:
  print(1+int(x11)*2)
  exit()
