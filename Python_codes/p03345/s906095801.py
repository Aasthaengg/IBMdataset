a, b, c, k = map(int, input().split())

if k % 2 == 1:
    print(b - a)
elif k % 2 == 0:
    print(a - b)