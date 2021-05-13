n, d = map(int, input().split())
scope = 2 * d + 1
if n % scope != 0:
    print(n // scope + 1)
else:
    print(n // scope)