def actual(a, b, x):
    if a <= x <= a + b:
        return 'YES'

    return 'NO'

a, b, x = map(int, input().split())
print(actual(a, b, x))