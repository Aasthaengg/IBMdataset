num1,num2 = input().split()
num = int(num1 + num2) ** (1/2)
if num % 1 == 0:
  print('Yes')
else:
  print('No')