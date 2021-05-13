a,b,c = map(int,input().split())
if(c-b>a): 
  print("dangerous")
elif(c-b<=0): 
  print("delicious")
else:
  print("safe")
