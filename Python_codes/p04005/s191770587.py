a,b,c=map(int,input().rstrip().split(' '))
if(a%2==0 or b%2==0 or c%2==0):
  print(0)
else:
  x=min(a*b,b*c,c*a)
  print(x)