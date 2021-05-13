a, b, k = map(int, input().split())


while k > 0:
    if a % 2 == 1:
        a -= 1
    a, b = a // 2, b + a // 2
    k -= 1
    if k > 0:
        if b % 2 == 1:
            b -= 1
        b, a = b // 2, a + b // 2
        k -= 1

print(a, b)
