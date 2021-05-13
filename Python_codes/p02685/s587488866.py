# n choose 0, n choose 1, ..., n choose kすべて一気に求める
def binomials_p(n, k, p):
    '''
    Input: integers n, k such that n >= k >= 0, prime number p
    Output: [n choose 0 mod p, n choose 1 mod p, ..., n choose k mod p]
    '''
    binomials = [1, n] # binomial[i] = n choose i mod p
    inv = [0, 1] # inv[i] : inverse of i mod p
    for i in range(2, k + 1):
        inv.append(( inv[p % i] * (p - p//i) ) % p ) # inverse of i
        binomials.append(binomials[i - 1] * (n - i + 1) * inv[i] % p)

    return binomials

# a^n mod p
def exp_by_sq_p(a, n, p):
    if n == 0:
        exp = 1
    elif n == 1:
        exp = a % p
    elif  n % 2 == 0:
        exp = exp_by_sq_p(a * a % p, n // 2, p)
    else:
        exp = a * exp_by_sq_p(a * a % p, (n - 1) // 2, p) % p
    return exp % p

N, M, K = [int(x) for x in input().split()]
p = 998244353

binomials = binomials_p(N - 1, K, p)
ans = 0
pow = 1 # (m - 1)^0 mod p
for j in range(K + 1):
    ans = (ans + binomials[K - j] * pow % p) % p
    pow = pow * (M - 1) % p

ans = ans * M * exp_by_sq_p(M - 1, N - K - 1, p) % p

print(ans)