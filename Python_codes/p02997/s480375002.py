import sys

# stdin = open("testdata.txt", "r")
n, k = map(int, sys.stdin.readline().split())

def solve(n, k):
	mx = (n-1)*(n-2)//2
	isolated = [(i, j) for i in range(2, n) for j in range(i+1, n+1)]
	edges = [(1, j) for j in range(2, n+1)]
	while mx != k:
		edge = isolated.pop()
		edges.append(edge)
		mx -= 1
	return edges

if k > (n-1)*(n-2)//2:
	print(-1)
else:
	res = solve(n, k)
	print(len(res))
	for edge in res:
		print(*edge)