w, h, x, y = map(int, input().split())
ans = w * h / 2
n = 1 if w == x * 2 and h == y * 2 else 0
print(ans, n)