A, B = map(int, input().split())
div, rem = divmod(abs(A - B), 2)
print("IMPOSSIBLE" if rem else min(A, B) + div)
