N,K = list(map(int,input().split()))
mod = int(1e9+7)
d = dict()
ans = 0
for X in range(K,0,-1):
  res = pow(K//X,N,mod)
  for k in range(2*X,K+1,X):
    res -= d[k]
  d[X] = res%mod
  ans += (res*X)%mod
  
print(ans%mod)