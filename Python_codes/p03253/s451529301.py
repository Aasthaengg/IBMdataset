import math

# 素因数分解
def prime_factorization(n):
    # s * s <= n
    s = math.floor(math.sqrt(n)) # 平方根を小数点切り捨て
    ans = [] # [素数, 指数]のリスト

    # 2からsまでの素因数を求める
    for i in [2] + list(range(3, s + 1, 2)):
        if n < i:
            break
        if n % i == 0:
            r = 0 # 指数カウンタクリア
            while n % i == 0:
                r += 1
                n //= i
            ans.append([i, r])

    # 残った素数を追加
    if n > s:
        ans.append([n, 1])

    return(ans)

def binomial_p(n, k, p):
    '''
    Input: integers n, k such that n >= k >= 0, prime number p
    Output: n choose k mod p
    '''
    k = min(k, n-k)

    if k == 0:
        retval = 1
    elif k == 1:
        retval = n
    else:
        numer = n  # n * (n - 1) * ... * (n - k + 1)
        inv = [0, 1]    # inv[i] : inverse of i mod p
        inv_denom = 1 # factorial of inverse of k mod p = 1^(-1) * 2^(-1) * ... * k^(-1) mod p
        for i in range(2, k + 1):
            numer = numer * (n - i + 1) % p
            inv.append(( inv[p % i] * (p - p//i) ) % p ) # inverse of i
            inv_denom = inv_denom * inv[-1] % p
        retval = numer * inv_denom % p

    return retval

###########################

N, M = [int(x) for x in input().split()]
q = 10 ** 9 + 7

if M == 1:
    ans = 1
else:
    pfact = prime_factorization(M)
    ans = 1
    for pr in pfact:
        ans = ans * binomial_p(N - 1 + pr[1], pr[1], q) % q

print(ans)
