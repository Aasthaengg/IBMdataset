N, K = map(int, input().split())
P = list(map(int, input().split()))
E = [(p+1)/2.0 for p in P]
tmp = sum(E[0:K])
ans = tmp
for i in range(1, N-K+1):
    tmp = tmp - E[i-1] + E[i+K-1]
    ans = max(ans, tmp)
print(ans)