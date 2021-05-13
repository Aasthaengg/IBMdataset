N,A,B=map(int,input().split())
Z=0
for i in range(1,N+1):
  X=0
  Y=i
  for j in range(5):
    X+=Y%10
    Y//=10
  if A<=X and X<=B:
    Z+=i
print(Z)