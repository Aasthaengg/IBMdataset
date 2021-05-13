a, b, c = map(int, input().split())

ans = b
if (c - b) <= a:
    ans += c
else:
    ans += (a + b + 1)

print(ans)