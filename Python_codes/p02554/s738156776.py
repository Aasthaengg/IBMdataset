N=int(input())
mod=10**9+7
if N<=1:
  print(0)
else:
  print((pow(10,N,mod)-2*pow(9,N,mod)+pow(8,N,mod))%mod)