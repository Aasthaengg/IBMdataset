n, a, b = map(int, input().split())

if a > b:
    print(0)
    exit()
elif a != b and n == 1:
    print(0)
    exit()

print((b*(n-1)+a) - (a*(n-1)+b) + 1)
