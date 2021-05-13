a,b,c,d=map(int,raw_input().split())
if a+b<c+d:
  print "Right"
elif a+b>c+d:
  print "Left"
else:
  print "Balanced"