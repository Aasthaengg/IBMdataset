N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
flag = True
Sum = 0 
for i in range(N-1):
    for j in range(i+1, N):
        f = True
        for k in range(N):
            if k == i or k == j:
                continue
            if A[i][k] + A[k][j] < A[i][j]:
                flag = False
            elif A[i][k] + A[k][j] == A[i][j]:
                f = False
        if f:
            Sum += A[i][j]
if flag:
    print(Sum)
else:
    print(-1)