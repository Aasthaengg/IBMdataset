def actual(a, b, c):
    if (a + b) == c or (b + c) == a or (c + a) == b:
        return 'Yes'

    return 'No'

a, b, c = map(int, input().split())
print(actual(a, b, c))