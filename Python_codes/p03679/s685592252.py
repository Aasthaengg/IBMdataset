x, a, b = map(int, input().split())

now = b - a
if (now <= 0):
   print('delicious')
elif (now > 0 and now <= x):
   print('safe')
else:
   print('dangerous')
