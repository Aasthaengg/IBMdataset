import sys
input = sys.stdin.readline

# B - Path
route = []

for i in range(3):
	a, b = map(int, input().split())	
	route.append(a)
	route.append(b)

count = 0

for i in range(1, 5):
	if route.count(i) >= 2:
		count += 1

if count >= 2:
	print('YES')
else:
	print('NO')