N,H,W = map(int,input().split())
A = []
B = []
for i in range(N):
	a,b = map(int,input().split())
	A.append(a)
	B.append(b)
cnt = 0
for i in range(N):
	if A[i] >= H and B[i] >= W:
		cnt+=1
print(cnt)