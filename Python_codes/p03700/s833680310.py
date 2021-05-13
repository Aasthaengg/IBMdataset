n, a, b = map(int, input().split())
h = [int(input()) for _ in range(n)]
l = 0
r = 10 ** 10
c = a - b
while l + 1 != r:
    m = (l + r) // 2
    tmp = 0
    for i in range(n):
        if h[i] > b * m:
            tmp += ((h[i] - b * m) // c + (1 if (h[i] - b * m) % c else 0))
    if tmp > m:
        l = m
    else:
        r = m
print(r)