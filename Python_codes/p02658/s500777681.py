import sys

N = int(input())
A = list(map(int, input().split()))

if 0 in A:
	print(0)
	sys.exit()

tmp = 1
for i in range(N):
	tmp = tmp * A[i]
	if tmp > 1000000000000000000:
		print(-1)
		sys.exit()

print(tmp)