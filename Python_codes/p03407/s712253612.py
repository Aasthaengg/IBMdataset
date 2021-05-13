def actual(a, b, c):
    if a + b >= c:
        return 'Yes'

    return 'No'

a, b, c = map(int, input().split())
print(actual(a, b, c))