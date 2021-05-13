a,b,c = map(int,input().split())
ans = 0
if a+b > c-2:
  print(b+c)
else:
  print(a+2*b+1)