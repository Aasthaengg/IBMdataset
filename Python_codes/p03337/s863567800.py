a,b=map(int,raw_input().split())
if a+b>= a-b and a+b>= a*b:
  print a+b
elif a-b >= a+b and a-b >= a*b:
  print a-b
elif a*b>= a+b and a*b>=a-b:
  print a*b