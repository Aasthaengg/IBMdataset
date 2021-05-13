x, a, b = map(int, input().split())

if a-b>=0:
  print('delicious')
elif a-b<0 and x +(a-b)>=0:
  print('safe')
else:
  print('dangerous')