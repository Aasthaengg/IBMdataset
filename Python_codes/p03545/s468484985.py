D = input()
A = [int(D[0]),int(D[1]),int(D[2]),int(D[3])]
for i in range(2**3):
    B = A[::1]
    C = ["+"]*3
    for j in range(3):
        if (i >> j) & 1:
            B[j+1] *= -1
            C[j] = "-"
    if sum(B) == 7:
        print(f"{A[0]}{C[0]}{A[1]}{C[1]}{A[2]}{C[2]}{A[3]}=7")
        exit()