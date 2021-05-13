n = input()
a_list = [int(i) for i in input().split()]

add_or_not = [True if i%2==1 else False for i in a_list]
if sum(add_or_not) %2 == 1:
  print('NO')
else:
  print('YES')