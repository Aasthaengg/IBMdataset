from collections import Counter

def solve(n, m, a):
    b = [0] * n
    b[0] = a[0] % m
    for i in range(1, n):
        b[i] = (b[i-1] + a[i]) % m
    c = Counter(b)
    t = filter(lambda _:_>1, c.values())
    t = map(lambda _:_*(_-1), t)
    return c[0] + sum(t) // 2

n, m = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, m, a))