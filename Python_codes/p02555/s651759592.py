
def comb(n, k, fact, invfact, M):
    return fact[n] * invfact[k] * invfact[n-k] % M

def main():

    s = int(input())
    M = 10** 9 + 7
    fact = [0] * 4001
    invfact = [0] * 4001
    fact[0] = 1
    for i in range(1,4001):
        fact[i] = fact[i-1] * i % M

    invfact[-1] = pow(fact[-1], M - 2, M)
    for i in range(4001-1, 0, -1):
        invfact[i-1] = invfact[i] * i % M
    ans = 0
    # try:
    for n in range(1,s):
        if 3 * n > s:
            break
        ans += comb(s-3*n+n-1, n-1, fact, invfact, M)
        ans %= M
    # except :
    #     print(n)
    #     print(s-3*n+n-1)
    print(ans)
if __name__=='__main__':
    main()
