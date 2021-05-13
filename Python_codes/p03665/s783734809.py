n, p = map(int, input().split())
ns = list(map(int, input().split()))
ns = [i % 2 for i in ns]
ans = [0, 0]
def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result
c = ns.count(1)
ans[1] = sum(cmb(c, i) for i in range(1, c + 1, 2)) * 2 ** (n - c)
ans[0] = 2**n - ans[1]
print(ans[p])