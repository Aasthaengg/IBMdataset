def abc058_a():
    a, b, c = map(int, input().split())
    if (b - a) == (c - b):
        print("YES")
    else:
        print("NO")


abc058_a()