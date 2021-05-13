
import sys
def input():
	return sys.stdin.readline().strip()

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

B_num = []
a = 0
for i in range(N):
	while a < N and A[a] < B[i]:
		a += 1
	if a == N:
		B_num.append(N)
	else:
		B_num.append(a)

for i in range(1, N):
	B_num[i] += B_num[i - 1]


C_num = []
b = 0
for i in range(N):
	while b < N and B[b] < C[i]:
		b += 1
	if b == N:
		C_num.append(B_num[-1])
	elif b > 0:
		C_num.append(B_num[b - 1])
print(sum(C_num))