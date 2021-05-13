N = input()
A = []
for i in xrange(N):
	A.append(input())
ans = 0
start = 0
for i in xrange(N):
	if A[i] > i - start:
		ans = -1
		break
	if A[i] > A[i-1] + 1:
		ans = -1
		break
	if i == 0:
		continue
	if A[i] == A[i - 1] + 1:
		ans += 1
		continue
	if A[i] == 0:
		start = i
		continue
	ans += A[i]
print ans

