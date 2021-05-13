N, K = map(int, input().split())
A = list(map(int, input().split()))
for k in range(K):
    B = [0] * N
    for n in range(N):
        l = max(0, n- A[n])
        r = min(N-1, n+A[n])
        B[l] += 1
        if r +1 < N:
            B[r+1] -= 1
    #print(B)
    for i in range(N-1):
        B[i+1] += B[i]
    #print(B)
    if sum(A) == N**2:
        break
    else:
        A = B[:]
print(*A)