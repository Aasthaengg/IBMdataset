N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = str(input())
A = []
count = 0

for i in range (0, N):
	if T[i] == 'r':
		A.append('p')
	elif T[i] == 's':
		A.append('r')
	else:
		A.append('s')

for i in range (K, N):
	if A[i] == A[i-K]:
		A[i] = 'd'

for i in range (0, N):
	if A[i] == 'r':
		count+=R
	if A[i] == 's':
		count+=S
	if A[i] == 'p':
		count+=P
        
print(count)