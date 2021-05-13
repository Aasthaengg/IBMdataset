n, k = map(int, input().split())

# k=0 -> n*n
if k == 0:
	print(n * n)
	exit()

cnt = 0
for b in range(1, n + 1):
	r_cnt = max(0, b - k)
	cnt += (n // b) * r_cnt
	if n % b >= k:
		cnt += (n % b) - k + 1

print(cnt)
