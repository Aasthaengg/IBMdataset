def actual(a, b, c):
    return min((a + b), (b + c), (c + a))

a, b, c = map(int, input().split())
print(actual(a, b, c))