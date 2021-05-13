N, K = map(int, input().split())

if K == 0:
    ans = N ** 2
    print(ans)
    exit()
    
ans = 0
for i in range(K+1, N+1):
    d = N // i
    m = N % i
    ans += (i - K) * d + max(m-K+1, 0)

print(ans)
