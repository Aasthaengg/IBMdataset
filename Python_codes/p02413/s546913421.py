r,c = map(int,input().split())
t = 0
A = [[]for i in range(r+1)]
for i in range(r):
	A[i]=list(map(int,input().split()))
for i in range(r):
	A[i].append(sum(A[i]))
for i in range(c+1):
	t=0
	for j in range(r):
		t += A[j][i]
	A[r].append(t)
for i in range(r+1):
	print(' '.join(map(str,A[i])))
