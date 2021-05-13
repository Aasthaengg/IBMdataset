n = int(input())
A, B = [], []
for i in range(n):
	a, b = map(int, input().split())
	A.append(a)
	B.append(b)

A = A[::-1]
B = B[::-1]

cnt = 0
for i in range(n):
	if (cnt + A[i]) % B[i] == 0:
		continue
	else:
		cnt += B[i] - (cnt + A[i]) % B[i]

print(cnt)