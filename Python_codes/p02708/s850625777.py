N, K = map(int, input().split())

ans = 0


for i in range(K, N+2):
    mi = ((i-1)*i)//2
    ma = N*i-mi
    ans += ma-mi+1
    ans %= 10**9+7
    # print(mi, ma)

print(ans)
