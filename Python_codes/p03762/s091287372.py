import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


N,M = MI()
X,Y = LI(),LI()
mod = 10**9+7

r = sum((i*(N-i)*(X[i]-X[i-1])) % mod for i in range(1,N))
r %= mod

ans = 0
for i in range(1,M):
    ans += r*i*(M-i)*(Y[i]-Y[i-1]) % mod
    ans %= mod

print(ans)
