
a, b, c = map(int, input().strip().split())
a_temp = a

for i in range(b):
    if a_temp % b == c:
        print('YES')
        break
    a_temp += a
else:
    print('NO')
