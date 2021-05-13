a, b, k = map(int, input().split())

while k:
    if a%2 == 1:
        a -= 1
    b += a//2
    a = a//2
    k -= 1
    if k > 0:
        if b%2 == 1:
            b -= 1
        a += b//2
        b = b//2
        k -= 1
print(a, b)