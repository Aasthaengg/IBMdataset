x,a,b=map(int,raw_input().split())
if a>=b:
  print "delicious"
elif b<=a+x:
  print "safe"
else:
  print "dangerous"