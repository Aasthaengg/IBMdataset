n, a, b = map(int, raw_input().split())
print min(a, b), max(0, a + b - n)