a,b=map(int,input().split())

if a<=5:
  print(0)
elif 6<=a<=12:
  print('{}'.format(b//2))
else:
  print("{}".format(b))