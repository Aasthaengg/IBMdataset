x1, y1, x2, y2 = list(map(int, input().split()))
vec12 = [x2 - x1, y2 - y1]
print(x2 - vec12[1], y2 + vec12[0], x1 - vec12[1], y1 + vec12[0])
