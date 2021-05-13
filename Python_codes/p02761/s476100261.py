N, M = map(int, input().split())
V = [-1]*N

if M == 0 and N == 1:
	print(0)
	exit()

for i in range (0, M):
	A, B = map(int, input().split())
	if V[A-1] == -1 or V[A-1] == B:
		V[A-1] = B
	else:
		print(-1)
		exit()
        
if V[0] == 0 and len(V) > 1:
	print(-1)
	exit()

for i in range (0, N):
	if V[i] == -1:
		if i ==0:
			V[i] = 1
		else:
			V[i] = 0

print(*V, sep="")