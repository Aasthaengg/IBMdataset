from math import gcd
N, M = map(int, input().split())
S = input()
T = input()
G = gcd(N, M)
 
for i in range(G):
    if S[i * N // G] != T[i * M // G]:
        print(-1)
        exit()
 
l = N * M // G
print(l)