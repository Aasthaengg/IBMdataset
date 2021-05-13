a, b = map(int, input().split())

ans = 0
if a < b:
    ans += b
    b -= 1
else:
    ans += a
    a -= 1
print(max(a, b) + ans)