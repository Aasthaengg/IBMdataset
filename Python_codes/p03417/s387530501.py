a,b = map(int, input().split())
a,b = (a,b) if a<=b else (b,a)
if (a == 1) :
  if (b == 1):
    print(1)
  else:
    print(b -2)
else :
  print((a-2)*(b-2))