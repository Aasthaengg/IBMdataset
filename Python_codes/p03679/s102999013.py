x, a, b  = map(lambda x: int(x),  input().split())
 
if b <= a:
  print('delicious')
elif x >= b - a:
  print('safe')
else:
  print('dangerous')