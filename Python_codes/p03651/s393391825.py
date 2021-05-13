from fractions import gcd

N,K = map(int, input().split())
A = [int(i) for i in input().split()]

M = max(A)

G = 0
for a in A:
    G = gcd(G, a)

if K % G == 0 and K <= M:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")