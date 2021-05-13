N, K = map(int, input().split())
V = [0]*N
*V, = map(int, input().split())

ans = []
for i in range(N+1):
    for j in range(N+1):
        if i+j > min(N, K): continue
        out = V[:i] + V[N-j:]
        out.sort()
        r = 0
        while i+j+r < K and r < len(out):
            if out[r] < 0: r += 1
            else: break
        ans.append(sum(out[r:]))

print(max(ans))