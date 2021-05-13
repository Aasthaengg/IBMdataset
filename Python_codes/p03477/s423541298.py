def actual(a, b, c, d):
    L, R = a + b, c + d

    if L > R:
        return 'Left'
    if L < R:
        return 'Right'

    return 'Balanced'

a, b, c, d = map(int, input().split())

print(actual(a, b, c, d))