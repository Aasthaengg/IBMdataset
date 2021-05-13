N, K, S = map(int, input().split())
A = [S for _ in range(N)]
for k in range(K, N):
    A[k] = 10**5+1
A = list(map(str, A))
print(" ".join(A))