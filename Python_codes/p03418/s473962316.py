N,K = map(int, input().split())

ans = 0

if K != 0:
    for b in range(K+1,N+1):
        ans += (b-K)*(N//b) + max(N%b-K+1, 0)
    print(ans)
else:
    print(N*N)