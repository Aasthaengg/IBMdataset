n,k=map(int,input().split())
if k%2==1:
  print((n//k)**3)
else:
  j=n//(k//2)
  if j %2==0:
    print(2*((j//2)**3))
  else:
    print(((j//2)**3)+((j//2+1)**3))
          
