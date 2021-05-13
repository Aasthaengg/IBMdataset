N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = 0
c = 0
aa = 0
for a in A:
	ans += B[a - 1]
	if a - 1 == aa:
		ans += c
	aa = a
	c = C[a - 1] if a < N else 0
print(ans)
