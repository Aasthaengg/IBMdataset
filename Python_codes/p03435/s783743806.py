C = [[int(_) for _ in input().split()] for _ in range(3)]

B = C[0]
A = (0, C[1][1] - B[1], C[2][2] - B[2])

for i in range(3):
    for j in range(3):
        v = A[i] + B[j]
        if not v == C[i][j]:
            print("No")
            exit(0)
print("Yes")
