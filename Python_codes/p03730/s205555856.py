a, b, c = map(int, input().split())

for i in range(1, b+1):
    k, r = divmod(a*i, b)
    if r == c:
        print('YES')
        break
else:
    print('NO')