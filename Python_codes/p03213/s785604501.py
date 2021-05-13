def prime_factors(n):
    i = 2
    factors = []
    while i**2 <= n:
        if n % i != 0:
            i += 1
        else:
            factors.append(i)
            n = n // i
    if n > 1:
        factors.append(n)
    return factors

def resolve():
    N = int(input())
    factors = []
    for i in range(1, N+1):
        factors.extend(prime_factors(i))
    import collections
    cnter = collections.Counter(factors)
    
    n_over_74 = 0
    n_over_24 = 0
    n_over_14 = 0
    n_over_4 = 0
    n_over_2 = 0
    for k, cnt in cnter.items():
        if cnt >= 74:
            n_over_74 += 1
        if cnt >= 24:
            n_over_24 += 1
        if cnt >= 14:
            n_over_14 += 1
        if cnt >= 4:
            n_over_4 += 1
        if cnt >= 2:
            n_over_2 += 1
    
    ans = 0
    if n_over_74 >= 1:
        ans += n_over_74
    if n_over_4 >= 1 and n_over_14 >= 1:
        ans += n_over_14*(n_over_4-1)
    if n_over_24 >= 1 and n_over_2 >= 1:
        ans += n_over_24*(n_over_2-1)
    if n_over_4 >= 2 and n_over_2 >= 3:
        ans += int((n_over_4*(n_over_4-1)/2)*(n_over_2-2))
    print(ans)

    
        

if '__main__' == __name__:
    resolve()