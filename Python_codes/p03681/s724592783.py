n,m = map(int, input().split())
mod = 1000000007
def fac(a,mod):
    res = 1
    for i in range(1,a+1):
        res *= i
        res %= mod
    return res
if n==m:
    print(fac(n,mod) * fac(m,mod) * 2 % mod)
elif (n==m+1):
    print(fac(n,mod) * fac(m,mod) % mod)
elif (n+1==m):
    print(fac(n,mod) * fac(m,mod) % mod)
else:
    print(0)