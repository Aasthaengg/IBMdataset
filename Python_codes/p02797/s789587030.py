N, K, S = [int(_) for _ in input().split()]

a = [S for _ in range(K)]
if S != 1:
    b = [S - 1 for _ in range(N-K)]
else: 
    b = [S + 1 for _ in range(N-K)]

print(" ".join([str(v) for v in a + b]))
