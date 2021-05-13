a, b = map(int, input().split())
ans = 0
if a >= 13:
    print(b)
elif 5 < a <= 12:
    print(b // 2)
else:
    print(0)
