N,M = map(int,input().split())
A = [list(map(int,input().split())) for i in range(N)]

A.sort()
sm = 0
cnt = 0

i = 0
while sm != M:
	cnt += A[i][0]*min(A[i][1],M-sm)
	sm += min(A[i][1],M-sm)
	i += 1

print(cnt)