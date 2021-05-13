import math
def primes(n):
    max = math.sqrt(n)
    candidates = [i for i in range(2, n+1)]
    primes = []
    while candidates[0] <= max:
        primes.append(candidates[0])
        candidates = [candidates[i] for i in range(len(candidates)) if candidates[i] % candidates[0] != 0]
    primes.extend(candidates)
    return primes

def resolve():
    N = int(input())
    _primes = primes(55555)
    ans = []
    for p in _primes:
        if p%5==1:
            ans.append(p)
            if len(ans) == N:
                break
    print(" ".join(map(str, ans)))

    
if '__main__' == __name__:
    resolve()
