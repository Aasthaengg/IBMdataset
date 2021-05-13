a,b,c,d=map(int,raw_input().split())
if a*b>c*d:
  print a*b
elif c*d>a*b:
  print c*d
elif c*d==a*b:
  print (c*d + a*b)/2