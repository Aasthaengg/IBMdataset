from functools import reduce

def comb(n, r):
    if n < 0 or r < 0 or r > n:
        return 0
    r = min(r, n - r)
    if r == 0: return 1

    numer = [n - r + i + 1 for i in range(r)]
    denom = [i + 1 for i in range(r)]

    for i in range(1, r):
        divisor = denom[i]
        if divisor > 1:
            offset = (n - r) % (i + 1)
            for j in range(i, r, i+1):
                numer[j - offset] //= divisor
                denom[j] //= divisor

    return reduce(lambda x, y: x*y if y > 1 else x, numer)

def sieve(n):
    a = [1] * (n + 1)
    a[0] = a[1] = False
    for i in range(4, n+1, 2):
        a[i] = False
    lim = int(n**0.5) + 1
    for i in range(3, lim + 1, 2):
        if a[i]:
            for j in range(i + i, n + 1, i):
                a[j] = False
    return a

N = int(input())

factors = []
sv = sieve(N)
for p in range(2, N+1):
    if sv[p]:
        n = N
        x = 0
        while n // p > 0:
            n //= p
            x += n
        if x > 0:
            factors.append([p, x])

# print(factors)
ans = 0
for xx in [[[4,2],[2,1]],[[14,1],[4,1]],[[24,1],[2,1]],[[74,1]]]:
    c = 1
    done = 0
    for i, x in enumerate(xx):
        s = sum(f[1] >= x[0] for f in factors)
        s = max(0, s - done)
        if s < x[1]:
            c = 0
            break
        else:
            c *= comb(s, x[1])
            done += x[1]
    ans += c

print(ans)