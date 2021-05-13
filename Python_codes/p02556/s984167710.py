n, *XY = map(int, open(0).read().split())
X, Y = XY[::2], XY[1::2]
A = [x+y for x, y in zip(X, Y)]
B = [x-y for x, y in zip(X, Y)]
A.sort()
B.sort()
print(max(A[-1] - A[0], B[-1] - B[0]))