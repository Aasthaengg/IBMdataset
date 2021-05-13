pay = int(input())
one_coin = int(input())
amari = pay%500
if amari <= one_coin:
  print('Yes')
else:
  print('No')