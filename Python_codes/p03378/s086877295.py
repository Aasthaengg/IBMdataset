N,M,X = map(int, input().split())
A = list(map(int, input().split()))

G = sum([a < X for a in A])

print(min(G, M-G))