a,b,x=map(int,input().split())
if a>2:
  s=b//x
  t=(a-1)//x
  print(s-t)
elif a==1:
  print(b//x)
elif a==0:
  print(b//x+1)