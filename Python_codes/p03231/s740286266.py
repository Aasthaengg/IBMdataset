N, M = map(int, input().split())
S = str(input())
T = str(input())

if M > N:
	M, N = N, M
	S, T = T, S

import math
G = N*M//math.gcd(N, M)

A = []
B = []

C = N//math.gcd(N,M)
D = M//math.gcd(N,M)

for i in range (0, math.gcd(N,M)):
	if S[i*C] != T[i*D]:
		print(-1)
		exit()

print(G)