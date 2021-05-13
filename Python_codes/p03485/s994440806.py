a,b=map(int,input().split())

if a%2==0 and b%2==0:
  print(int((a+b)/2))
elif a%2==1 and b%2==1:
  print(int((a+b)/2))
elif a%2==0 and b%2==1:
  print(int((a+b+1)/2))
else:
  print(int((a+b+1)/2))