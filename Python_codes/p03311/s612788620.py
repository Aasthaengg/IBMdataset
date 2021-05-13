import sys
def input():
	return sys.stdin.readline().strip()

N = int(input())
A = list(map(int, input().split()))

for i in range(N):
	A[i] -= i + 1
A.sort()

med = A[N//2]

ans = 0
for i in range(N):
	ans += abs(A[i] - med)
print(ans)