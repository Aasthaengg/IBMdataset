def comb_mod(n,r,mod):
    a,b=1,1
    r = min(r,n-r)
    for i in range(r):
        a = a*(n-i) % mod
        b = b*(r-i) % mod
    return a * pow(b, mod-2, mod) % mod

def prime_factor(x):
    
    prime_factor=[]
    
    for i in range(2,int(x**0.5)+1):
        if x==1: break

        count = 0
        while x%i == 0:
            x //= i
            count += 1
        if count>0:
            prime_factor.append((i,count))
    
    if x>1: prime_factor.append((x,1))
    
    return prime_factor

MOD = 10**9 + 7

n,m=map(int,input().split())

m_fac = prime_factor(m)

ans = 1
for value,count in m_fac:
    ans = (ans * comb_mod(count+n-1,count,MOD)) %MOD
print(ans)