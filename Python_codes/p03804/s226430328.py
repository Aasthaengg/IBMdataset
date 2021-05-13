N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]


for i in range(N - M + 1):
    for j in range(N - M + 1):
        check = True
        count = 0
        for k in range(M):
            if (A[i + k][j: j + M] == B[k]):
                # print(A[i + k][j:j + M], B[k])
                count += 1
                continue
            else:
                check = False
                break

        if (check and count == M):
            print('Yes')
            exit()

print('No')
