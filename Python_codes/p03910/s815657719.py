Score = int(input())

Numero = 0

for i in range (1, 10000000):
	if i*(i+1)/2 >= Score:
		Numero = i
		break

K = Numero

P = []

for i in range (0, K):
	if Score >= (K-i):
		P.append(K-i)
		Score = Score - (K-i)

P = reversed(P)

print(*P, sep = "\n") 