x1, y1, x2, y2 = map(float, input().split())
A = [x1, y1]
B = [x2, y2]
dict = sum((a - b) ** 2 for a, b in zip(A, B))
print("{:.8f}".format(dict ** 0.5))

