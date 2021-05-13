MAX = 10 ** 5
def sieve(n):
    f = [False] * (n + 1)
    res = []
    for i in range(2, n+1):
        if f[i]:
            continue
        res.append(i)
        for j in range(2 * i, n+1, i):
            f[j] = True
    return res

pn = sieve(MAX)
acc = [0] * (MAX + 1)
for p in pn:
    if p % 2 == 1 and (p + 1) // 2 in pn:
        acc[p] = 1
for i in range(2, MAX+1):
    acc[i] += acc[i-1]
Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(acc[r] - acc[l-1])
