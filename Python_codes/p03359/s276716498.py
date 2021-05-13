a, b = map(int, input().split())
ans = 0
ans += a
if a > b:
    ans -= 1
print(ans)