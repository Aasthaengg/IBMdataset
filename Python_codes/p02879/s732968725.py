a, b = map(int, input().split())
ans = -1

if a >= 10 or b >= 10:
    print(ans)
else:
    ans = a*b
    print(ans)