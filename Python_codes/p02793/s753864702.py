from collections import defaultdict
MOD = 10**9+7
n = int(input())
A = list(map(int, input().split()))


def factorization(n):
    retval = []
    tmp = n
    for i in range(2, int(-(-n**.5//1))+1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            retval.append((i, cnt))
    if tmp != 1:
        retval.append((tmp, 1))
    return retval


x = defaultdict(int)
for a in A:
    for p, q in factorization(a):
        if x[p] < q:
            x[p] = q

mod_x = 1
for p, q in x.items():
    mod_x *= pow(p, q, MOD)
mod_x %= MOD

B = [mod_x*pow(a, MOD-2, MOD) % MOD for a in A]
print(sum(B) % MOD)
