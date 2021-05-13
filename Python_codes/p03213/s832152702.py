import bisect
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
    l = [0] * (N+1)
    for i in range(1, N+1):
        a = prime_factorize(i)
        for j in a:
            l[j] += 1
    l = l[2:]
    l.sort()
    r = 0
    a = bisect.bisect_left(l, 2)
    b = bisect.bisect_left(l, 4)
    c = bisect.bisect_left(l, 14)
    d = bisect.bisect_left(l, 24)
    e = bisect.bisect_left(l, 74)
    if e < N-1:
        r += N - e - 1
    if d < N-1:
        r += (N - d - 1) * (N - a - 2)
    if c < N-1:
        r += (N - c - 1) * (N - b - 2)
    if b < N-2:
        r += (N - a - 3) * (N - b - 1) * (N - b - 2) // 2
    print(r)
main()
