import bisect

N = int(input())
[A, B, C] = [sorted([int(i) for i in input().split()]) for j in range(3)]
ans = 0
for j in B:
	ans += bisect.bisect_left(A, j) * (N-bisect.bisect_right(C, j))
print(ans)
