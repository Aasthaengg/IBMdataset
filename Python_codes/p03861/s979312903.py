def cnt(n, x):
    if n < 0:
        return 0
    return n // x + 1

a, b, x = map(int, input().split())
print(cnt(b, x) - cnt(a - 1, x))