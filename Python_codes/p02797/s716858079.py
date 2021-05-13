N, K, S = map(int, input().split())
if S!=10**9:
    A = [S+1]*N
    for i in range(K):
        A[i] -= 1

    for c in A:
        print(c, end=" ")
else:
    A = [1]*N
    for i in range(K):
        A[i] = S
    for c in A:
        print(c, end=" ")