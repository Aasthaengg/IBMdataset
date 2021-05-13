def actual(a, b):
    if a == b:
        return 'H'

    return 'D'

a, b = input().split()
print(actual(a, b))