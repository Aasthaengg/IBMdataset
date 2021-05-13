def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    sumA = sum(A)
    
    for i in range(N):
        res = B[i]
        if A[i] > 0 and res != 0:
            A[i], res = max(A[i] - res, 0), max(res - A[i], 0)

        if A[i+1] > 0 and res != 0:
            A[i+1], res = max(A[i+1] - res, 0), max(res - A[i+1], 0)
    
    print(sumA - sum(A))
    return

resolve()