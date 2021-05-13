n,k=list(map(int,input().split()))
a=list(map(int,input().split()))
if n<=k:
  print(1)
  exit()
n=n-k
if n%(k-1)==0:
  print(1+n//(k-1))
else:
  print(1+n//(k-1)+1)