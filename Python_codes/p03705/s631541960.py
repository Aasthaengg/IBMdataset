n, a, b = map(int, input().split())

if n >= 2:
    if a < b:
        ans = a + b * (n - 1) - (a * (n - 1) + b) + 1
    elif a == b:
        ans = 1
    else:
        ans = 0
else:
    if a < b:
        ans = 0
    elif a == b:
        ans =1
print(ans)