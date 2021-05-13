def ff(n):
    i = 1
    r = set()
    while i * i <= n:
        if n % i == 0:
            r.add(i)
            if i != n // i:
                r.add(n // i)
        i += 1
    return sorted(r)

def main():
    N, K = map(int, input().split())
    mod = 10**9 + 7
    T = [[] for _ in range(K + 1)]
    F = [ff(i) for i in range(K + 1)]
    for i, f in enumerate(F[1:], 1):
        for j in f:
            T[j].append(i)
    r = 0
    t = [0] * (K + 1)

    for i in reversed(range(1, K + 1)):
        q = (pow(len(T[i]), N, mod) - t[i]) % mod
        for j in F[i][:-1]:
            t[j] = (t[j] + q) % mod
        r = (r + i * q) % mod

    return r

print(main())
