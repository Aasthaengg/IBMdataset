n = list(map(int, input().split()))
if n[1] - n[2] >= 0:
  print('delicious')
elif n[2] - n[1] <= n[0]:
  print('safe')
else:
  print('dangerous')