N,K = map(int,input().split())
ans = 0
for k in range(K,N+2):
    ans += N*k-k*(k-1)/2-k*(k-1)/2+1
ans %= 10**9+7
print(int(ans))