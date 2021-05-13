N = int(input())
A = [int(A) for A in input().split()]
for k in range(N):
    if k == N -1:
        print("{}".format(A[k]))
    else:
        print("{}".format(A[k]), end = " ")
for i in range(1, N):
    j = i -1
    v = A[i]
    while j >= 0 and A[j] > v:
        A[j+1] = A[j]
        j -= 1
    A[j+1] = v
    for k in range(N):
        if k == N -1:
            print("{}".format(A[k]))
        else:
            print("{}".format(A[k]), end = " ")