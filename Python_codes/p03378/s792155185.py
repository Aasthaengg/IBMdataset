N, M, X = map(int,input().split())
A = list(map(int,input().split()))

G_0 = 0
G_N = 0
for a in A:
    if a < X:
        G_0 += 1
    else:
        G_N += 1

print(min(G_0,G_N))