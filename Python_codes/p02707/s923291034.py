N = int(input())
num = [0] * (3 * 10 ** 5)
A = list(map(int,input().split()))
for i in range(len(A)):
	num[A[i]] += 1
for i in range(1,N + 1):
	print(num[i])