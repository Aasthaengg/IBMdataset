n, a, b = map(int, input().split())
if (b-a)%2 != 0:
    if a-1 <= n-b:
        ans = (b - a -1)//2 + 1 + a-1
    else:
        ans = (b - a - 1)//2 + 1 + n-b
else:
    ans = min((b - a) // 2, b-1, n-a)
print(ans)