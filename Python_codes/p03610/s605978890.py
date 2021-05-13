S = str(input())

P = []

for i in range (0, len(S)):
	if i%2==0:
		P.append(S[i])

cosmos = P[0]

for i in range (1, len(P)):
	cosmos+=P[i]

print(cosmos)