a,b,c=map(int,input().split())
if a%2==0 or b%2==0 or c%2==0:
  print(0)
else:
  temp=max(a,b,c)//2  
  print(min(a,b,c)*(a+b+c-min(a,b,c)-max(a,b,c))*abs(temp-max(a,b,c)+temp))