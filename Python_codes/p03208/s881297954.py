n, k = map(int, input().split())
H = sorted([int(input()) for i in range(n)])
minv = float('inf')
for x, y in zip(H, H[k-1:]):
	minv = min(minv, y - x)
print(minv)