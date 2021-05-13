N, K = map(int, input().split())
V = list(map(int, input().split()))
ans = 0

for i in range(N+1):
    for j in range(N+1):
        if i+j>N:
            continue
        
        l = []
        
        for k in range(i):
            l.append(V[k])
        
        for k in range(j):
            l.append(V[N-1-k])
        
        if len(l)>K:
            continue
        
        l.sort()
        cnt = K-len(l)
        now = 0
        
        while cnt>0 and now<len(l) and l[now]<0:
            cnt -= 1
            now += 1
        
        ans = max(ans, sum(l[now:]))

print(ans)