N, M = list(map(int,input().split()))
A = input().split()
jikan = 0
for i in range(M):
	jikan += int(A[i])
if N - jikan >= 0:
	print(N - jikan)
else:
	print(-1)