n, a, b = map(int, input().split())

x = (b-a) % 2
if x == 1:
    ans = 0
    if (a-1) < (n-b):
        d = a-1
        y = b - d
        ans += d
        ans += (y + 1) // 2
    else:
        d = n-b
        y = a + d
        ans += d
        ans += (n-y + 1) // 2
    ans = min([ans, b-1, n-a])
    print(ans)
else:
    print((b-a+1)//2)
