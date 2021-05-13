N = int(input())
A = list(map(int,input().split()))

cnt = 0

for i in range(N):
	#rint(A[i],i+1)
	if A[A[i]-1] == i+1:
		cnt += 0.5


print(int(cnt))