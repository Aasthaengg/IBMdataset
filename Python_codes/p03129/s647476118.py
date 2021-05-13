number_list = [int(i) for i in input().split()]

if number_list[0] % 2 == 0:#偶数のとき
  if number_list[0] >= number_list[1]*2:
    print('YES')
  else:
    print('NO')
else:
  if number_list[0] + 1 >= number_list[1]*2:
    print('YES')
  else:
    print('NO')