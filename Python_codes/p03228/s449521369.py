a, b, k = map(int, raw_input().split())

stop = 0

for i in range(k):
    if i % 2 == 0:
        a /= 2
        b += a
        if b == a * 2:
            stop = i + 1
            break
    if i % 2 == 1:
        b /= 2
        a += b
        if a == b * 2:
            stop = i + 1

if stop == 0 or (k - stop) % 2 == 0:
    print a, b
else:
    print b, a

