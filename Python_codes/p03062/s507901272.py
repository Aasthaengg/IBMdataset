N = int(input())
A = list(map(int, input().split()))

B = A.copy()

K = 0

for i in range (0, N):
	if A[i] < 0:
		B[i] = -1*B[i]
		K+=1

Tashita = sum(B)

if K%2 != 0:
	Tashita-=2*min(B)

print(Tashita)