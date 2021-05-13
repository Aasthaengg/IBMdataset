def actual(a, b, c, d):
    if abs(a - c) <= d:
        return 'Yes'

    if abs(a - b) <= d and abs(b - c) <= d:
        return 'Yes'

    return 'No'


a, b, c, d = map(int, input().split())
print(actual(a, b, c, d))