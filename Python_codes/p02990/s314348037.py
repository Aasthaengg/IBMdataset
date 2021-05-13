n, k = map(int, input().split())
MOD = 10**9+7
red_num = n - k
blue_num = k

def prepare(n, MOD):
    """
    nCr mod MOD
    n!/r!/(n-r)! → facts(n)*invs(r)*invs(n-r)
    :param n:
    :param MOD:
    :return:
    """
    facts = [1]*(n+1)
    for i in range(1, n+1):
        facts[i] = facts[i-1]*i%MOD
    invs = [1]*(n+1)
    _invs = [1]*(n+1)
    invs[n] = pow(facts[n], MOD-2, MOD)
    for i in range(0, n)[::-1]:
        invs[i] = invs[i+1] * (i+1) % MOD
    return facts, invs

for i in range(1, k+1):
    if red_num+1 < i:
        print(0)
        continue
    facts1, inves1 = prepare(red_num+1, MOD)
    facts2, inves2 = prepare(k-1, MOD)
    a = facts1[red_num+1]*inves1[i]*inves1[red_num+1-i]%MOD
    b = facts2[k-1]*inves2[i-1]*inves2[k-i]%MOD

    print(a*b%MOD)


