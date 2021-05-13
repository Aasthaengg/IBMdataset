n , a, b = map(int, input().split())

if b < a:
    print(0)
    exit()

if n == 1:
    if a != b:
        print(0)
        exit()
    else:
        print(1)
        exit()

print((n-2) * (b-a) + 1)
