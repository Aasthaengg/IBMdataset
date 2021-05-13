a, b, c, d = (int(_) for _ in input().split())
print('Left' if a + b > c + d else 'Right' if a + b < c + d else 'Balanced')