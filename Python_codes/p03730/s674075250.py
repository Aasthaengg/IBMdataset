a, b, c = map(int, input().split())

n = a
cnt = 1
while cnt <= b:
    if n % b == c:
        print('YES')
        exit()
    cnt += 1
    n += a
print('NO')