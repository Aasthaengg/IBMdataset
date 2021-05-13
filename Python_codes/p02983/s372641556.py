L,R=map(int,input().split())
mod=2019
if L%mod >= R%mod or R-L >= mod:
  print(0)
else:
  a=mod
  for i in range(L%mod,R%mod):
    for j in range(i+1,R%mod+1):
      a=min((i*j)%mod,a)
  print(a)