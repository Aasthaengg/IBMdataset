N,M,X = map(int, input().split())
A = list(map(int, input().split()))

G = [0] * (N+1)
for a in A: G[a] = 1
print(min(sum(G[:X]), sum(G[X:])))