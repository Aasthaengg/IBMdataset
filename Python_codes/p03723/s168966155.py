a, b, c = map(int, input().split())
ans = 0

while True:
    if a%2==1 or b%2==1 or c%2==1:
        print(ans)
        break
    if a == b == c:
        print(-1)
        break
    s = a // 2
    t = b // 2
    u = c // 2
    a, b, c = t+u, s+u, s+t
    ans += 1
else:
    print(ans)