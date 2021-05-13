n,a,b = map(int,input().split())
if(a>b):
  print(0)
else:
  if(n == 1):
    if(a!=b):
      print(0)
    else:
      print(1)
  else:
    print(b*(n-1)+a-(a*(n-1)+b)+1)
  
