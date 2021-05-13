def actual(n, a, b):
    return min(n * a, b)

n, a, b = map(int, input().split())
print(actual(n, a, b))