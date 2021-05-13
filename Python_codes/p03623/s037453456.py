x,a,b = map(int, input().split())

a_dis = abs(x-a)
b_dis = abs(x-b)

if a_dis<b_dis:
  print('A')
else:
  print('B')