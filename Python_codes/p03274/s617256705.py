N, K = map(int, input().split())
X = [int(i) for i in input().split()]

X_n = sorted([-x for x in X if x < 0])
X_p = sorted([x for x in X if x >= 0])

ans = 10**20
for k in range(K+1):
    if len(X_n) >= k and len(X_p) >= K-k:
        if k == 0:
            ans = min(ans, X_p[K-1])
        elif k == K:
            ans = min(ans, X_n[K-1])
        else:
            ans = min(ans, 2*X_n[k-1] + X_p[K-k-1], X_n[k-1] + 2*X_p[K-k-1])
print(ans)
