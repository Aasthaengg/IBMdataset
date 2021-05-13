N, M = list(map(int, input().split()))
A = []
B = []
for _ in range(N):
    A.append(input())
for _ in range(M):
    B.append(input())

# print(A)
# print(B)

# i = 行、j = 列
for i in range(N - M + 1):
    for j in range(N - M + 1):
        # print(i, j)
        A_part = []
        for k in range(i, i + M):
            A_part.append(A[k][j:j + M])
        # print(A_part)
        if A_part == B:
            print("Yes")
            exit()
print("No")
