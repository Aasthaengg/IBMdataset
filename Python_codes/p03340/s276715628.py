N = int(input())
A = list(map(int, input().split()))
x = r = res = 0
for l in range(N):
	while r < N:
		if x & A[r]: break
		x += A[r]
		r += 1
	res += r - l
	x -= A[l]
print(res)