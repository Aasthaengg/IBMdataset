from bisect import bisect_left, bisect_right
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

cnt = 0
for j in range(n):
	idx_i = bisect_left(A, B[j])
	idx_k = bisect_right(C, B[j])
	cnt += idx_i * (n - idx_k)

print(cnt)