x,y = map(int,input().split())

if (2*x-y)%3 != 0 or 2*x-y < 0:
    print(0)
    exit()

b = (2*x-y)//3
a = x-2*b

if a < 0:
    print(0)
    exit()

mod = 10**9+7

def prepare(n, mod):
    facts = [1]*(n+1)
    for i in range(1, n+1):
        facts[i] = facts[i-1]*i%mod
    invs = [1]*(n+1)
    invs[n] = pow(facts[n], mod-2, mod)
    for i in range(0, n)[::-1]:
        invs[i] = invs[i+1] * (i+1) % mod
    return facts, invs
facts,invs = prepare(a+b,mod)
def make_combi(facts,invs,n,r,mod):
    return facts[n]*invs[r]*invs[n-r]%mod
print(make_combi(facts,invs,a+b,a,mod))