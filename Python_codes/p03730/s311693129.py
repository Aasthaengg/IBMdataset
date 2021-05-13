a, b, c = map(int, input().split())
l = []
for i in range(1,101):
    if a*i%b == c:
        print('YES')
        exit()
print('NO')