import math
N,M = map(int,input().split())
S = input()
T = input()
L = N * M // math.gcd(N,M)
NN = L // N
MM = L // M

for i in range(10**6):
    if MM*i > len(S)-1 or NN*i > len(T)-1:
        break
    if S[i*MM] != T[i*NN]:
        print(-1)
        exit()
print(L)