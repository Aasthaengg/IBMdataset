def resolve():
    n = int(input())
    def divisor(n):
        ass = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                ass.append(i)
                if i ** 2 == n:
                    continue
                ass.append(n // i)
        return ass  # sortされていない
    g = sorted(divisor(n))

    q = []
    for i in range(1, len(g)):
        m=n
        while m >= g[i]:
            if m %g[i] == 0:
                m = m//g[i]
            else:
                m = m%g[i]
        if m == 1:
            q.append(g[i])
    print(len(set(divisor(n-1)+q))-1)

resolve()