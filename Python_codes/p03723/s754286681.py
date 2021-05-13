a, b, c = map(int, input().split())
if a == b == c:
    if a % 2:
        print(0)
    else:
        print(-1)
else:
    ans = 0
    while a % 2 == b % 2 == c % 2 == 0:
        ans += 1
        a, b, c = b // 2 + c // 2, a // 2 + c // 2, a // 2 + b // 2
    print(ans)
