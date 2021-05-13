N,K = map(int,input().split())
#ans[i]=上からi個の和-下からiこの和+1 i個選んだ和の種類
ans = 0
mod = 10**9+7
for i in range(K,N+2):
    if i*2 > N+1:
      #print(i,(N+1-i)*N+1 % mod)
      ans += (N+1-i)*i+1 % mod
    else:
      #print(i,(N-i+1)*i+1 % mod)
      ans += (N-i+1)*i+1 % mod
print(ans%mod)
