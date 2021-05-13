import math
def make_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors
def main():
    N, K = map(int, input().split())
    mod = 10**9 + 7
    d = {}
    r = 0
    for i in range(K, 0, -1):
        l = make_divisors(i)
        x = K // i
        t = pow(x, N, mod)
        if i in d:
            t -= d[i]
        for j in l:
            if j not in d:
                d[j] = t
            else:
                d[j] += t
        r += t * i
        r %= mod
    return r % mod
print(main())
