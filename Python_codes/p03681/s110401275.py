def s(n,m):
  f = 1
  for i in range(1,n+1):f*=i;f%=m
  return f
N,M=map(int,input().split());m=10**9+7
print(s(N,m)*s(M,m)*(2-(N+M)%2)%m if abs(N-M) < 2 else 0)