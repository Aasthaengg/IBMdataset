def resolve():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    C = []
    D = []
    for __ in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    for i in range(N):
        count = abs(A[i]-C[0]) + abs(B[i]-D[0])
        ans = 1
        for j in range(1, M):
            if count > abs(A[i]-C[j]) + abs(B[i]-D[j]):
                count = abs(A[i]-C[j]) + abs(B[i]-D[j])
                ans = j+1
        print(ans)
resolve()