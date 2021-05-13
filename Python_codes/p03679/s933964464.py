x,a,b = (int(i) for i in input().split())
if a < b:
  if b-a > x:
    print ('dangerous')
  else:
    print ('safe')
else:
  print ('delicious')