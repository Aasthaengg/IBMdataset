def actual(a, b):
    if (a * b) % 2 == 0:
        return 'Even'

    return 'Odd'

a, b = map(int, input().split())
print(actual(a, b))
