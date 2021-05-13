N, K = map(int, input().split())
p = list(map(int, input().split()))
ans = (sum(p[0:K])+K)/2
pre = ans
for i in range(1, N-K+1):
    pre -= (p[i-1]-p[i+K-1])/2
    ans = max(pre, ans)
print(ans)
