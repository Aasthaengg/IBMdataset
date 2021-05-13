n, *XY = map(int, open(0).read().split())
X, Y = XY[::2], XY[1::2]
A = [x+y for x, y in zip(X, Y)]
B = [x-y for x, y in zip(X, Y)]
print(max(max(A) - min(A), max(B) - min(B)))