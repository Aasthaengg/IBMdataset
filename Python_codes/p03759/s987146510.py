def actual(a, b, c):
    if (b - a) == (c - b):
        return 'YES'

    return 'NO'

a, b, c = map(int, input().split())
print(actual(a, b, c))