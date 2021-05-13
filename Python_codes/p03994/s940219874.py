S = str(input())
K = int(input())

N = len(S)

L = []

for i in range (0, N):
	L.append((97-ord(S[i]))%26)

W = []

for i in range (0, N-1):
	if L[i] <= K:
		W.append('a')
		K -= L[i]
	else:
		W.append(S[i])

V = (26-L[N-1]+K)%26
W.append(chr(97+V))
print(*W, sep="")