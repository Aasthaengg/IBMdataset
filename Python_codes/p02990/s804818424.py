def prepare(n, MOD):
    # 1! - n! の計算
    f = 1
    factorials = [1]  # 0!の分
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    # n!^-1 の計算
    inv = pow(f, MOD - 2, MOD)
    # n!^-1 - 1!^-1 の計算
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv

    return factorials, invs
    #nCr = (factorials[n]%MOD * invs[r]%MOD * invs[n-r]%MOD)%MOD
def main2():
    n,k=map(int, input().split())
    MOD = 10**9 + 7
    facs,invs = prepare(n+k,MOD)
    red = n-k
    j=0
    blue = 0
    # . R . R . R . R .
    #仕切りで考えると仕切りの数はN-k+1
    #1からj個まで
    for i in range(1,k+1):
        tmp = (facs[red+1]%MOD * invs[i]%MOD * invs[red+1-i]%MOD)%MOD * (facs[k-1]%MOD * invs[i-1]%MOD * invs[k-i]%MOD)%MOD
        if(red+1-i<0):
            tmp = 0
        print(tmp%MOD)

if __name__ == '__main__':
    main2()
