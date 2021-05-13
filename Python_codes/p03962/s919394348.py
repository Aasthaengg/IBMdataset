def actual(a, b, c):
    return len({a, b, c})

a, b, c = map(int, input().split())
print(actual(a, b, c))