n,k = map(int,input().split())
V = list(map(int,input().split()))
ans = 0
for i in range(n+1):
    for j in range(n+1-i):
        removed = V[:i] + V[n-j:]
        if len(removed) > k:break
        removed.sort()
        get = sum(removed)
        for l in range(min(k-len(removed),len(removed))):
            if removed[l] >= 0:break
            get -= removed[l]
        ans = max(ans,get)
print(ans)
