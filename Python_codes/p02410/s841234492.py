N,M = map(int, input().split())
A = []
for i in range(N):
    I = list(map(int, input().split()))
    A.append(I)

b = []
for i in range(M):
    bi = []
    I = int(input())
    bi.append(I)
    b.append(bi)

for i in range(N):
    result = 0
    for j in range(M):
        result += A[i][j] * b[j][0]
    print(result)