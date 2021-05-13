c = [list(map(int, input().split())) for _ in range(3)]
a1 = 0
b1 = c[0][0]
a2 = c[1][0] - b1
a3 = c[2][0] - b1
b2 = c[1][1] - a2
b3 = c[2][2] - a3
A = [a1, a2, a3]
B = [b1, b2, b3]

for i in range(3):
    for j in range(3):
        if c[i][j] != A[i]+B[j]:
            print("No")
            exit(0)

print("Yes")