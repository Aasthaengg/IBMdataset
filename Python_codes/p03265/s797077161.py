a, b, c, d = map(int, input().split())
dx = c - a
dy = d - b
print(str(str(c-dy) + " " + str(d+dx) + " " + str(a-dy) + " " + str(b+dx)))