N, *A = map(int, open(0).read().split())

ans = [0] * N
for i in range(N):
    ans[0] += (-1) ** i * A[i]
    
for i in range(1, N):
    ans[i] = (A[i - 1] - ans[i - 1] // 2) * 2
    
print(*ans)
