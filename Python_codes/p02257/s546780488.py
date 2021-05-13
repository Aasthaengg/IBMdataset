# Aizu Problem ALDS_1_1_C: Prime Numbers
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")

def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]

primes = primes2(10000)

def is_prime(k):
    if k in primes:
        return True
    r = math.sqrt(k)
    for p in primes:
        if k % p == 0:
            return False
        if p > r:
            return True
    return True

N = int(input())
cnt = 0
for _ in range(N):
    k = int(input())
    if is_prime(k):
        cnt += 1
print(cnt)