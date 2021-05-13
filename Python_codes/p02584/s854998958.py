x,k,d=map(int,input().split())
x=abs(x)

if x>=k*d:
  print(x-k*d)
elif (k-x//d)%2==0:
  print(x-x//d*d)
else:
  print((x//d+1)*d-x)