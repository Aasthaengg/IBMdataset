N,K = map(int,input().split())
V = list(map(int,input().split()))

ans = 0
for l in range(N):
    if l > K: break
    for r in range(N-l+1):
        if l+r > K: break
        vs = V[:l] + (V[-r:] if r>0 else [])
        vs.sort()
        k = K-l-r
        t = 0
        for v in vs:
            if v < 0 and k > 0:
                k -= 1
                continue
            t += v
        ans = max(ans,t)
print(ans)