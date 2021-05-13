def actual(a, b):
    if a <= b:
        return a

    return a - 1

a, b = map(int, input().split())
print(actual(a, b))