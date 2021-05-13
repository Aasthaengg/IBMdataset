def prepare(n, MOD):

    # n! の計算
    f = 1
    for m in range(1, n + 1):
        f *= m
        f %= MOD
    fn = f
    
    # n!^-1 の計算
    inv = pow(f, MOD - 2, MOD)
    # n!^-1 - 1!^-1 の計算
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
    
    return fn, invs

def solve(x,y):
    MOD=10**9+7
    if (x+y)%3!=0:
        return 0
    L=(x+y)//3
    if x<L or y<L:
        return 0
    i=min(x,y)-L
    if i==0 or i==L:
        return 1
    fn,invs=prepare(L,MOD)
    ret=(fn*invs[i])%MOD
    ret=(ret*invs[L-i])%MOD
    return ret

x,y=map(int,input().split())
print(solve(x,y))