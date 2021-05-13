a, b, c = map(int, input().split())

ka = a
m = ka % b
while True:
    if ka % b == c:
        print('YES')
        exit(0)
    ka += a
    if ka % b == m:
        break
print('NO')
