N, M = map(int, input().split())
A = [list(input()) for i in range(N)]
B = [list(input()) for i in range(M)]
flag = False

for x1 in range(N - M + 1):
    for x2 in range(N - M + 1):
        check = True
        for y in range(M):
            for z in range(M):
                if A[z + x1][y + x2] != B[z][y]:
                    check = False

                # print(A[z][y])
                # print(B[z][y])
        if check:
            flag = True
            break

if flag:
    print("Yes")
else:
    print("No")
