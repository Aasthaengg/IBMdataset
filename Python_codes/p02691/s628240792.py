from bisect import bisect_left, bisect_right

N = int(input())

A = list(map(int, input().split()))
Ap = [i - A[i] for i in range(N)]
Ap.sort()

ans = 0
for i in range(N):
	ans += bisect_right(Ap, i + A[i]) - bisect_left(Ap, i + A[i])

print(ans)