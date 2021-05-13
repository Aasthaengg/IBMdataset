a,b,c=map(int,input().split())
if a<b<c and a<c-b:
  print("dangerous")
elif a>=b>=c:
  print("delicious")
else: 
  print("safe")