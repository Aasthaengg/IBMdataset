N,K = map(int,input().split())
mod = 10**9+7


def p(m,n):
    a = 1
    for i in range(n):
        a = a*(m-i)
    return a

def p_mod(m,n,mod):
    a = 1
    for i in range(n):
        a = a*(m-i) % mod
    return a

def c(m,n):
    return p(m,n) // p(n,n)

def c_mod(m,n,mod):
    return (p_mod(m,n,mod)*pow(p_mod(n,n,mod),mod-2,mod)) % mod


for i in range(1,K+1):
    print((c_mod(N-K+1,i,mod) * c_mod(K-1,i-1,mod)) % mod)