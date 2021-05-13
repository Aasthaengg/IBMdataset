a, b, c = map(int, input().split())
ans = 0
first = min(b, c)
b -= first
c -= first
ans += first * 2
if b == 0 and c == 0:
    pass
elif b == 0:
    if a == c:
        ans += c
    elif a > c:
        ans += c
    else:
        ans += a+1
else:
    ans += b
print(ans)