def actual(a, b, x):
    if a > x:
        return 'NO'

    if a + b >= x:
        return 'YES'

    return 'NO'

a, b, x = map(int, input().split())
print(actual(a, b, x))