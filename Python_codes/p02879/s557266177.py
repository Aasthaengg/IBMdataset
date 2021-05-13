a, b = map(int, input().split())

if a == 0 or a >= 10 or b == 0 or b >= 10:
    print(-1)
else:
    print(a*b)