N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

passed = 0
for i in range(N):
    num = 0

    for j in range(M):
        num += A[i][j] * B[j]
    num += C

    if num > 0:
        passed += 1

print(passed)
