a, b = map(int, input().split())
print("IMPOSSIBLE" if (a + b) % 2 else int((a + b) / 2))