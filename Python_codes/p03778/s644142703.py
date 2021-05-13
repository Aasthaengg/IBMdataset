w, a, b = map(int, input().split())
ans = 0
if a > b:
    ans = a - b - w
else:
    ans = b - a - w
if ans < 0:
    print(0)
else:
    print(ans)