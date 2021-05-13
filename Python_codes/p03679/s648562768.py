x,a,b=map(int,input().split())
# a mae b go
syomi=b-a
if syomi <= 0:
  print("delicious")
elif syomi>=(x+1):
  print("dangerous")
else:
  print("safe")