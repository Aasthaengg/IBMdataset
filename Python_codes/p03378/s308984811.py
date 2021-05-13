N, M, X = map(int, input().split())
A = list(map(int, input().split()))
C = [False] * (N + 1)
for a in A:
    C[a] = True
print(min(sum(C[:X]), sum(C[X:])))