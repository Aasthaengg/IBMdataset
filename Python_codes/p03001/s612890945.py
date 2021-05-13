w, h, x, y = map(int, input().split())
print(float(w) * float(h) / 2, 1 if (w == x + x) & (h == y + y) else 0)
