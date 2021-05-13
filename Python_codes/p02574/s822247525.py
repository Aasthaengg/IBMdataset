def e_coprime():
    from math import gcd
    from functools import reduce
    N = int(input())
    A = [int(i) for i in input().split()]

    def sieve(n):
        ret = list(range(n + 1))
        for j in range(2, int(n**0.5) + 1):
            for k in range(j, n + 1, j):
                if k == ret[k]:
                    ret[k] = j
        return ret

    d = sieve(max(A))
    prime_factor = set()
    for a in A:
        t = set()
        while a > 1:
            t.add(d[a])
            a //= d[a]
        if prime_factor & t:
            break
        prime_factor |= t
    else:
        return 'pairwise coprime'

    if reduce(lambda x, y: gcd(x, y), A) == 1:
        return 'setwise coprime'
    return 'not coprime'

print(e_coprime())