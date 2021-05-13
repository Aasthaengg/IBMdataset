N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]
isIn = False
for i in range(N - M + 1):
    for j in range(N - M + 1):
        isOK = True
        for now in range(M):
            if A[i+now][j:j+M] != B[now]:
                isOK = False
                break
        if isOK:
            isIn = True
            break
    if isIn:
        break
if isIn:
    print("Yes")
else:
    print("No")
