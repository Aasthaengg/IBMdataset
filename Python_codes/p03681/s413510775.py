import sys
MOD = pow(10,9)+7
N,M = map(int,input().split())
if N < M:
  N,M = M,N

if abs(N-M) >1 :
  print(0)
  sys.exit()
  
if N == M:
  ans = 2
  while N>0 and M>0:
    ans = ans*M*N%MOD
    M -= 1; N -= 1
else:
  if N == M:
    ans = 2
    while N>0 and M>0:
      ans = ans*M*N%MOD
      M -= 1; N -= 1
  else:
    ans = N
    N -= 1
    while N>0 and M>0:
      ans = ans*M*N%MOD
      M -= 1; N -= 1
print(ans)