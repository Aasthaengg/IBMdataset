a, b, K = map(int, input().split())

for i in range(K):
    if i %2 == 0:
        if a % 2 == 1: a -= 1
        b += a // 2
        a //= 2
    else:
        if b % 2 == 1: b -= 1
        a += b // 2
        b //= 2
print(a, b)
