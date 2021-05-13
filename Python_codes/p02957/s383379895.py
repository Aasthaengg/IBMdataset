a,b=map(int,input().split())
if a%2==0 and b%2==0:
  print((a+b)//2)
  
elif a%2!=0 and b%2!=0:
  print((a+b)//2)
  
else:
  print('IMPOSSIBLE')