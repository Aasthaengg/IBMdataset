n, r = map(int, input().split())
ans = 0

if n < 10:
    ans = 100 * (10 - n) + r
    print(ans)
else:
    ans = r
    print(ans)