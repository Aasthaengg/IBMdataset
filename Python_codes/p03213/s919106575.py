from collections import Counter
from operator import mul
from functools import reduce
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def main():
    N = int(input())
    factors = [1]
    for i in range(1, N+1):
        factors += prime_factorize(i)
    cnt = Counter(factors)
    cntlst = list(cnt.values())
    
    count74 = sum([1 for val in cntlst if val>=74])
    count24 = sum([1 for val in cntlst if val>=24])
    count14 = sum([1 for val in cntlst if val>=14])
    count4  = sum([1 for val in cntlst if val>=4])
    count2  = sum([1 for val in cntlst if val>=2])
    
    ans = count74 + count24*(count2-1) + count14*(count4-1) \
                + (count4*(count4-1)*(count2-2))//2
    print(ans)

main()