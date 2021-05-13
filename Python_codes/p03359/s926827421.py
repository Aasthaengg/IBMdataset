a, b = map(int, input().split())

if a == 1 and b == 1:
    print(1)
    exit()

if a <= b:
    print(a)
else:
    print(a-1)