N, K = map(int, input().split())
A = list(map(int, input().split()))
A = A + [0]

if K >= N - 1:
    ans = [N] * N
    print(*ans)

else:
    for i in range(K):
        tmp = [0] * (N + 1)
        
        for j in range(N):
            end_l = max(j - A[j], 0)
            end_r = min(j + A[j] + 1, N)
            
            tmp[end_l] += 1
            tmp[end_r] -= 1
        
        flg = tmp[0]
        
        for j in range(1, N):
            tmp[j] += tmp[j - 1]
            flg += tmp[0]
            A[j] = tmp[j]
        
        A[0] = tmp[0]
        
        if flg == N**2:
            break
            
    print(*A[:N])