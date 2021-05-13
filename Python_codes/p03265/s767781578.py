x1, y1, x2, y2 = map(int, input().split())
dx, dy = x2-x1, y2-y1
c = (x2-dy, y2+dx)
d = (x1-dy, y1+dx)
print(*c, *d)
