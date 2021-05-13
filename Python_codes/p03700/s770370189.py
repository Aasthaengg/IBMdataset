n, a, b = map(int, input().split())
h = [int(input()) for _ in range(n)]

l = 0
r = max(h) // b + 1
while r - l > 1:
    m = (l + r) // 2
    count = 0
    for x in h:
        x = x - m * b
        if x > 0:
            count += (x + a - b - 1) // (a - b)
    if count <= m:
        r = m
    else:
        l = m
print(r)