n = int(input())
d, x = map(int, input().split())
c = 0
for _ in range(n):
	a = int(input())
	for i in range(1, d+1, a):
		c += 1
print(c + x)