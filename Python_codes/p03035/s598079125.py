a, b = map(int, input().split())

if a >= 13:
    print(b)
elif a > 5 and a < 13:
    print(int(b/2))
else:
    print(0)