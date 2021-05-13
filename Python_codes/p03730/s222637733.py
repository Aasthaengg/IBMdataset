a, b, c = map(int, input().split())

n = 0
for i in range(10**6):
    n += a
    n %= b
    if n == c:
        print('YES')
        exit()

print('NO')