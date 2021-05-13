# K <= N(N-1)//2 - (N-1)
#    = (N-1)(N-2)//2

N, K = map(int, input().split())

if K > (N - 1) * (N - 2) // 2:
    print(-1)
else:
    M1 = N - 1
    M2 = (N - 1) * (N - 2) // 2 - K
    M = M1 + M2

    print(M)
    for i in range(1, N):
        print(N, i)
    m = 0
    for i in range(1, N):
        for j in range(i + 1, N):
            if m < M2:
                print(i, j)
                m += 1
            else:
                break
        if m == M2:
            break
