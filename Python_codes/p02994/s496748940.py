a,b=map(int,input().split())
if b>=0:
  print(int((a+2*b)*(a-1)/2))
elif a+b>0:
  print(int((a+2*b-1)*a/2))
else:
  print(int((a+2*b-2)*(a-1)/2))