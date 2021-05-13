import sys
input = sys.stdin.readline

# A - Painting
h, w, n = [int(input()) for i in range(3)]

if h > w:
	row = h
else:
	row = w

if n % row == 0:
	print(n // row)
else:
	print(n // row + 1)