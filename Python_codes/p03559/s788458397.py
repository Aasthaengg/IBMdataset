import bisect

N = int(input())
A = tuple(sorted(map(int, input().split())))
B = tuple(map(int, input().split()))
C = tuple(sorted(map(int, input().split())))
res = 0
for i in range(N):
	res += bisect.bisect_left(A, B[i])*(N - bisect.bisect_right(C, B[i]))
print(res)