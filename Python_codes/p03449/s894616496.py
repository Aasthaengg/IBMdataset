# input
N = int(input())
A = [list(map(int, input().split())) for i in range(2)]

# check
element = set(A[0] + A[1])
if len(element) == 1:
    print(list(element)[0] * (N + 1))
else:
    res = 0
    for d in range(N):
        if d == 0:
            sum_num = A[0][0] + sum(A[1])
        elif d == N - 1:
            sum_num = sum(A[0]) + A[1][N - 1]
        else:
            sum_num = sum(A[0][:d + 1]) + sum(A[1][d:])
        if res < sum_num:
            res = sum_num
    print(res)