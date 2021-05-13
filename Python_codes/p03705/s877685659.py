n, a, b = map(int, input().split())

ans = 0
if a > b:
    pass
elif n == 1:
    if a == b:
        ans = 1
    else:
        pass
else:
    ans = (b - a)*(n - 2) + 1
print(ans)