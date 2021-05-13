def primes(n):
    import math
    max = math.sqrt(n)
    candidates = [i for i in range(2, n+1)]
    primes = []
    while candidates[0] <= max:
        primes.append(candidates[0])
        candidates = [candidates[i] for i in range(len(candidates)) if candidates[i] % candidates[0] != 0]
    primes.extend(candidates)
    return primes

def resolve():
    X = int(input())
    _primes = primes(10**5+4)
    import bisect
    print(_primes[bisect.bisect_right(_primes, X)] if X not in _primes else X)



if '__main__' == __name__:
    resolve()