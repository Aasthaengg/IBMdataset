N = int(input())
A = [0] + [int(x) for x in input().split()] + [0]

B = []
for i in range(1,N+2) :
    B.append(abs(A[i] - A[i-1]))

C = []
for i in range(2,N+2) :
    C.append(abs(A[i] - A[i-2]))

tlen = sum(B)
for i in range(N) :
    print(tlen - B[i] - B[i+1] + C[i])
