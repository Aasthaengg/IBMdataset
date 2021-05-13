a, b = map(int, input().split())

if b == 1:
    print(0)
elif b <= a:
    print(1)
else:
    print((b - 2)//(a - 1) +1)