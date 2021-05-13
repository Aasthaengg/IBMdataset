N, M = map(int, input().split())

P = [0]*(N+1)

for i in range (0, M):
	A, B = map(int, input().split())
	P[A-1]+=1
	P[B]-=1
    
for i in range (1, N+1):
	P[i]+=P[i-1]
    
P = sorted(P, reverse = True)

count = 0

for i in range (0, N+1):
	if P[i] == M:
		count+=1
	else:
		print(count)
		exit()