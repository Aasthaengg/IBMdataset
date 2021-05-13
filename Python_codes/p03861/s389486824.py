a, b, x = [int(s) for s in input().split()]
q, m = divmod(a, x)
print(b // x - q + (1 if m == 0 else 0))