a, b, k = list(map(int, input().split()))
for i in range(k):
    if i % 2 == 0:
        if a % 2 == 1:
            a -= 1
        tmp_a = a//2
        a -= tmp_a
        b += tmp_a
    if i % 2 == 1:
        if b % 2 == 1:
            b -= 1
        tmp_b = b//2
        b -= tmp_b
        a += tmp_b

print(a, b)
