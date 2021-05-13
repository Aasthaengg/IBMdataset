def actual(a, b, c):
    if a == b:
        return c
    if b == c:
        return a
    if c == a:
        return b

a, b, c = map(int, input().split())
print(actual(a, b, c))
