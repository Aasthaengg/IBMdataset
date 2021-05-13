def actual(a, b):
    return max((a + b, a - b, a * b))

a, b = map(int, input().split())
print(actual(a, b))