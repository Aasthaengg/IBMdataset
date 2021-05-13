N, M = map(int, input().split())
A = []
B = []
for _ in range(N):
    A.append(list(input()))
for _ in range(M):
    B.append(list(input()))

for i in range(N - M + 1):
    for j in range(N - M + 1):
        # match
        flag = True
        for k in range(M):
            for l in range(M):
                if A[i + k][j + l] == B[k][l]:
                    pass
                else:
                    flag = False

        if flag:
            break

    if flag:
        break

if flag:
    print("Yes")
else:
    print("No")
