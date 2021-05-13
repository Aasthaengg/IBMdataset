N = int(input())
P = [int(input()) for i in range(N)]
L = max(P)
G = L // 2
V = 0
for i in range(N):
        V += P[i]
F = V - L
print(G + F)