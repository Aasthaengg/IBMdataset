a,b,c = map(int,input().split())
if b+c >= a:
  print(int(c-a+b))
else:
  print('0')