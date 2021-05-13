from collections import Counter

def solve(n, m, a):
    b = [0] * n
    b[0] = a[0] % m
    for i in range(1, n):
        b[i] = (b[i-1] + a[i]) % m
    c = Counter(b)
    res = c[0]
    for num in c.values():
        if num > 1:
            res += num * (num-1) // 2
    return res

n, m = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, m, a))