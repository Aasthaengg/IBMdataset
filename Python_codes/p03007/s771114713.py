N = int(input())
A = list(map(int, input().split()))

A.sort()
S = sum(A)

if A[0] >= 0:
    print(S - A[0] * 2)
    tmp = A[0]
    for i in range(1, N - 1):
        print(tmp, A[i])
        tmp -= A[i]
    print(A[-1], tmp)

elif A[-1] <= 0:
    print(-S + A[-1] * 2)
    tmp = A[-1]
    for i in range(1, N):
        print(tmp, A[~i])
        tmp -= A[~i]

else:
    op = []
    tmp1 = A[-1]
    i = 1
    while A[i] < 0:
        op.append((tmp1, A[i]))
        tmp1 -= A[i]
        i += 1
    tmp2 = A[0]
    i = 1
    while A[~i] >= 0:
        op.append((tmp2, A[~i]))
        tmp2 -= A[~i]
        i += 1
    print(tmp1 - tmp2)
    for x, y in op:
        print(x, y)
    print(tmp1, tmp2)