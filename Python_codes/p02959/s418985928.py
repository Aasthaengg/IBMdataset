N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

monster = 0

for i in range(N):

    if A[i] >= B[i]:
        monster += B[i]
        A[i] -= B[i]
        B[i] = 0

    else:
        monster += A[i]
        B[i] -= A[i]
        A[i] = 0

        if A[i + 1] >= B[i]:
            A[i + 1] -= B[i]
            monster += B[i]
            B[i] = 0

        else:
            monster += A[i + 1]
            B[i] -= A[i + 1]
            A[i + 1] = 0


# print(A)
# print(B)
print(monster)