import sys
input = sys.stdin.readline

# B - Robot Arms
n = int(input())
robots = []

for i in range(n):
	x, l = map(int, input().split())
	left = x - l
	right = x + l
	robots.append([left, right])

robots.sort(key=lambda x: x[1])
prev_robot = -sys.maxsize
ans = 0

for r in robots:
	if r[0] >= prev_robot:
		ans += 1
		prev_robot = r[1]

print(ans)