num1, num2, num3 = map(int,input().split())

num_group = [num1, num2, num3]

if (num1 + num2 + num3)/2 in num_group:
  print('Yes')
else:
  print('No')