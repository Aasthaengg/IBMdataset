w, a, b = map(int, input().split())

ans = b - (a + w)
ans1 = a - (b + w)

if a <= b:
    print(max(ans, 0))
else:
    print(max(ans1, 0))