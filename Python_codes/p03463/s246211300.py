import sys
input = sys.stdin.readline

# A - Move and Win
n, a, b = map(int, input().split())

if (b - a) % 2 == 0:
	print('Alice')
else:
	print('Borys')