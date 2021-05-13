n = int(input())
a = [0] * n
for v in map(int, input().split()):
	a[v - 1] += 1
for v in a:
	print(v)