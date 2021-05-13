kMax = 100000
def calc_primes():
    is_prime = [True] * (kMax+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, kMax+1):
        if not is_prime[i]:
            continue
        for k in range(2*i, kMax+1, i):
            is_prime[k] = False
    ans = []
    for i in range(2, kMax+1):
        if is_prime[i]:
            ans.append(i)
    return ans

a = [0] * (kMax+1)

primes = set(calc_primes())

acc = 0
for i in range(1, kMax+1, 2):
    ii = (i+1)//2
    if i in primes and ii in primes:
        acc += 1
    a[i] = acc

Q = int(input())

for _ in range(Q):
    l, r = map(int, input().split())
    ra = a[r]
    la = a[l-2] if l >= 3 else 0
    print(ra-la)