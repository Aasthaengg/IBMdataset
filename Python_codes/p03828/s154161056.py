mod = 10**9+7
from collections import defaultdict
def sieve(N):
    prime = [0]*(N+1)
    isprime = [True]*(N+1)
    isprime[0]=isprime[1] = False
    num = 0
    for p in range(2,N+1):
        if isprime[p]:
            prime[num] = p
            num += 1
            for j in range(2*p,N+1,p):
                isprime[j] = False
    prime.sort()
    prime.reverse()
    for k in range(N-1):
        if prime[k+1] == 0:
            end = k
            break
    return prime[:end+1]

def main():
    N = int(input())
    if N == 1:
        print(1)
        exit()
    prime = sieve(N)
    prime.reverse()
    lis = defaultdict(int)
    for i in range(1,N+1):
        t = i
        for p in prime:
            if p > i:continue
            if t%p == 0:
                while t%p == 0:
                    t //= p
                    lis[p] += 1
    ans = 1
    for l in lis.values():
        ans *= (l+1)
        ans %= mod
    
    print(ans)

    

if __name__ == "__main__":
    main()