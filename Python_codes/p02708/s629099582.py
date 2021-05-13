N,K = map(int,input().split())
mod = 10**9+7

def cul(N,K):
  Ans = 0
  for i in range(N+1-K+1):
    t = (K+i-1)*(K+i)/2
    Ans += (K+i)*N - 2*t +1
  return(int(Ans%mod))

print(cul(N,K))
