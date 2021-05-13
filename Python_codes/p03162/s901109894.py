N = int(input())
A = [0]*N
B = [0]*N
C = [0]*N
for i in range(N):
    A[i], B[i], C[i] = map(int, input().split())

pointA = [0]*N; pointB = [0]*N; pointC = [0]*N
pointA[0] = A[0]; pointB[0] = B[0]; pointC[0] = C[0]
for i in range(1, N):
    pointA[i] = max(pointB[i-1], pointC[i-1]) + A[i]
    pointB[i] = max(pointA[i-1], pointC[i-1]) + B[i]
    pointC[i] = max(pointA[i-1], pointB[i-1]) + C[i]
print(max((pointA[N-1], pointB[N-1], pointC[N-1])))