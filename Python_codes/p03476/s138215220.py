import itertools

isPrime = [True]*(10**5+1)
similar = [0]*(10**5+1)
isPrime[0] = False
isPrime[1] = False
def sieve(n):
    for i in range(2, n+1):
        if isPrime[i]:
            if isPrime[(i+1)//2]:
                similar[i] = 1
            for j in range(i*2, n+1, i):
                isPrime[j] = False

sieve(10**5)

acm = list(itertools.accumulate(similar))

Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    ans = acm[r] - acm[l-1]
    print(ans)




