N,K= map(int,input().split(' '))

ans = 0
for b in range(K+1,N+1):
    k = N // b
    res = N - k*b
    ans += k * (b-K)
    if res >= K:
        ans += res - K + (K!=0)

print(ans)

