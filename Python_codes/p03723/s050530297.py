a, b, c = map(int, input().split())
if a == b and b == c:
    if a % 2 == 0:
        print(-1)
    else:
        print(0)
else:
    count = 0
    while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        a, b, c = (b + c) // 2, (c + a) // 2, (a + b) // 2
        count += 1
    print(count)