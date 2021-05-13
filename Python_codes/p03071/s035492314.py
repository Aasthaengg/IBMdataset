a, b = map(int, input().split())
ans = 0
if a >= b:
    ans += a
    a -= 1
else:
    ans += b
    b -= 1
if a >= b:
    print(ans + a)
else:
    print(ans + b)