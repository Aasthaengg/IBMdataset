n, d = map(int, input().split())

ans = 0
while n > 0:
    n -= 2 * d + 1
    ans += 1
print(ans)