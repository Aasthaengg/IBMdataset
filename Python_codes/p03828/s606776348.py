
def prime_factorize(N):
    res = [0] * (N+1)
    for n in range(2,N+1):
        a = 2
        while a*a <= n:
            if n % a == 0:
                ex = 0
                while n % a == 0:
                    ex += 1
                    n //= a
                #res.append((a, ex))
                res[a] += ex
            a += 1
        if n != 1:
            res[n] += 1
    return res

N = int(input())
prime = prime_factorize(N)

mod = 10 ** 9 + 7
ret = 1
for i in prime:
    ret *= (i+1)
    ret %= mod

print(ret)
