a, b, k = map(int, input().split())
while True:
    if a % 2 == 1:
        a -= 1
    b += a // 2
    a //= 2
    k -= 1
    if not k:
        break
    if b % 2 == 1:
        b -= 1
    a += b // 2
    b //= 2
    k -= 1
    if not k:
        break
print(a, b)
