def solve(a, b, k):
    for i in range(k):
        if i % 2 == 0:
            if a % 2 == 1:
                a -= 1
            b += a // 2
            a //= 2
        else:
            if b % 2 == 1:
                b -= 1
            a += b // 2
            b //= 2
    return "%d %d" % (a, b)

a, b, k = map(int, input().split())
print(solve(a, b, k))