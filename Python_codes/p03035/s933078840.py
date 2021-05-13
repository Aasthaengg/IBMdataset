a,b=map(int,input().split())

if 13<=a:
  p=int(b)
  print(p)
if 6<=a<=12:
  p=int(b//2)
  print(p)
if a<=5:
  print('0')