A = [list(map(int,input().split())) for i in range(3)]

N = int(input())

for n in range(N):
    B = int(input())

    for i in range(3):
        for j in range(3):
            if A[i][j] == B:
                A[i][j] = 0

for i in range(3):
    if (A[i][0] == 0 and A[i][1] == 0) and A[i][2] == 0:
        print("Yes")
        exit()

    elif (A[0][i] == 0 and A[1][i] == 0) and A[2][i] == 0:
        print("Yes")
        exit()

if (A[0][0] == 0 and A[1][1] == 0) and A[2][2] == 0:
    print("Yes")

elif (A[0][2] == 0 and A[1][1] == 0) and A[2][0] == 0:
    print("Yes")

else:
    print("No")