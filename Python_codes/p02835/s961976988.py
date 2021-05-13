a_list = list(map(int,input().split()))

a_sum = sum(a_list)

if a_sum <= 21:
  print('win')
else:
  print('bust')
