import sys
def input():
	return sys.stdin.readline().strip()


N = int(input())
A = input()
B = input()
C = input()

ans = 0

for i in range(N):
	if A[i] == B[i] and B[i] == C[i]:
		ans += 0
	elif A[i] == B[i] or B[i] == C[i] or C[i] == A[i]:
		ans += 1
	else:
		ans += 2

print(ans)