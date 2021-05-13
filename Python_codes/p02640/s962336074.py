import sys

x, y = map(int, input().split())

for i in range(x + 1):
	if (i * 2) + ( (x - i) * 4) == y:
		print('Yes')
		sys.exit()

print('No')