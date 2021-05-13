A,B = map(int, input().split())

ans = 0

for x in range(A, B + 1):
    x_1 = x % 10
    x = x // 10
    x_2 = x % 10
    x = x // 10
    x_3 = x % 10
    x = x // 10
    x_4 = x % 10
    x = x // 10
    x_5 = x % 10
    if (x_1 == x_5) and (x_2 == x_4):
        ans += 1

print(ans)