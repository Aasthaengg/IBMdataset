a, b = map(int, input().split())

ans = a+b

if ans > 23:
    ans = ans - 24

print(ans)