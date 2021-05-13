a,b=map(int,input().split())
if(a*2>=b):
  print(b//2)
else:
  print(a+(b-2*a)//4)