import sys
input = sys.stdin.readline

# A - Anti-Adjacency
N, K = map(int, input().split())
count = 0

for i in range(1, N + 1, 2):
	count += 1

if count >= K:
	print('YES')
else:
	print('NO')