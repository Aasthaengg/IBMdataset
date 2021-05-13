a, b, c = map(int, input().split())
ans = 0
if b < c:
    ans += 2 * b
    c -= b
    if c > a:
        ans += a + 1
    elif c == a:
        ans += c
    else:
        ans += c

else:
    ans = ans + b + c

print(ans)
