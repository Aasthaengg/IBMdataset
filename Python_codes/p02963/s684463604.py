s = int(input())

y1 = int(1e9)
x2 = s//y1 + (0 if s == int(1e18) else 1)

x1 = 1
y2 = x2*y1-s

ans = [0, 0, x1, y1, x2, y2]

print(" ".join(map(str, ans)))