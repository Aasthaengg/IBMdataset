D,N=map(int,input().split())
if N<100:
  print(100**D*N)
  exit()
print(100**D*101)