n, c = map(int, input().split())
a = [[0 for _ in range(c)] for _ in range(10 ** 5 + 1)]
for _ in range(n):
    s, t, u = map(int, input().split())
    a[s][u - 1] += 1
    a[t][u - 1] -= 1
m = 0
x = 0
for b in a:
    x += b.count(1)
    if x > m:
        m = x
    x -= b.count(-1)
print(m)