N = int(input())
A = [0]*N; B = [0]*N; C = [0]*N
for i in range(N):
    A[i], B[i], C[i] = map(int, input().split())

lisA = [0]*N; lisB = [0]*N; lisC = [0]*N
lisA[0] = A[0]; lisB[0] = B[0]; lisC[0] = C[0];
for i in range(1, N):
    lisA[i] = max(lisB[i-1], lisC[i-1]) + A[i]
    lisB[i] = max(lisA[i-1], lisC[i-1]) + B[i]
    lisC[i] = max(lisA[i-1], lisB[i-1]) + C[i]

print(max(lisA[N-1], lisB[N-1], lisC[N-1]))