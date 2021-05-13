a, b = map(int, input().split())
ans = 0
for _ in '__':
    if a > b:
        ans += a
        a -= 1
    else:
        ans += b
        b -= 1
print(ans)