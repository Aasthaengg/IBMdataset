W, a, b = map(int, input().split())

if b >= a:
    ans = b - a - W
else:
    ans = a - b - W

if ans <= 0:
    print(0)
else:
    print(ans)