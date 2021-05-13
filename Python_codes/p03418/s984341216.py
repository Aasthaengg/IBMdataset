N,K = map(int, input().split())

if K == 0:
    ans = N**2
else:
    ans = (N-K) * (N-K+1) // 2
    for b in range(K+1, N+1):
        q = (N-b+1) // b
        r = (N-b+1) % b
        ans += q*(b-K) + max(0, r-K)
        
print(ans)