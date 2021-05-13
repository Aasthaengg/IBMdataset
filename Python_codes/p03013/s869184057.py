from collections import Counter
n, m = map(int, input().split())
l = []
a0 = 0
for i in range(m):
    a = int(input())
    if a - a0 == 0:
        print(0)
        exit()
    l.append(a - a0 - 1)
    a0 = a + 1
l.append(n - a0)
d = Counter(l)
key = list(d.keys())

ma = max(key)
fib = [1]*(ma + 1)
for i in range(2, ma + 1):
    fib[i] = fib[i - 2] + fib[i - 1]

ans = 1
for k in key:
    ans *= fib[k]**d[k]
    ans %= 10**9 + 7

print(ans)