N, M = map(int, input().split())
A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(M)]

for s in range(N-M+1):
    for t in range(N-M+1):
        match = True
        for i in range(M):
            for j in range(M):
                if A[i+s][j+t] != B[i][j]:
                    match = False
                    break
            else:
                continue
            break
        if match:
            print('Yes')
            exit()
print('No')