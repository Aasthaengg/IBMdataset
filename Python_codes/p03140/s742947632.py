N = int(input())
A, B, C = input(), input(), input()

count = 0
for n in range(N):
	a, b, c = A[n], B[n], C[n]
	if a == b == c:
		continue
	if a == b or b == c or c == a:
		count += 1
		continue
	count += 2
print(count)
