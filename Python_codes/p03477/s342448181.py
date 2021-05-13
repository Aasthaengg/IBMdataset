a, b, c, d = map(int, input().split())
diff = a + b - c - d
print("Left" if diff > 0 else "Balanced" if diff == 0 else "Right")