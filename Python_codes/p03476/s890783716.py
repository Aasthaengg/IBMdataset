def primes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

mx = 10**5
ps = primes(mx)

valid = [0]*(mx+1)

for i in range(3,mx,2):
    if i in ps and (i+1)//2 in ps:
        valid[i] = 1

from itertools import accumulate
acc = list(accumulate(valid))

q,*lr = [list(map(int, s.split())) for s in open(0)]

for l,r in lr:
    print(acc[r] - acc[l-1])