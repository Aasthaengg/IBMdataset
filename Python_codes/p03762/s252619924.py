n , m= map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
mod = 10**9+7
def f(N,i):
  return (i*(N-i+1))%mod
def l(L,i):
  return (L[i]-L[i-1])%mod
def lf(L):
  N = len(L)
  return sum([(l(L,i)*f(N-1,i))%mod  for i in range(1,N)])
print(lf(x)*lf(y)%mod)