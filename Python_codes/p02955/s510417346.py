

import itertools

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


def resolve():
    N,K = map(int,input().split())
    A= list(map(int,input().split()))

    S = sum(A)
    
    divs = make_divisors(S)

    for d in divs[::-1]:
        r=[i%d for i in A]
        r.sort() 
        ruiseki = list(itertools.accumulate(r))
        for i,v in enumerate(ruiseki):
            b = ruiseki[-1]-v
            bb = (N-1-i)*d-b
            if v <= K and v == bb:
                print(d)
                return




resolve()
