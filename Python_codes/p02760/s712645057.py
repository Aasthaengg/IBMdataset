A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
Q = [int(input()) for _ in range(N)]

for q in Q:
    for i in range(3):
        for j in range(3):
            if A[i][j] == q:
                A[i][j] = 0

if A[0][0] == A[1][1] == A[2][2] == 0:
    print('Yes')
    exit()

if A[0][2] == A[1][1] == A[2][0] == 0:
    print('Yes')
    exit()

for i in range(3):
    if A[i][0] == A[i][1] == A[i][2] == 0:
        print('Yes')
        exit()

    if A[0][i] == A[1][i] == A[2][i] == 0:
        print('Yes')
        exit()

print('No')