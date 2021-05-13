a,b = map(int, input().split())
if (a+b)%2:
  print(int((a+b+1)/2))
else:
  print(int((a+b)/2))
