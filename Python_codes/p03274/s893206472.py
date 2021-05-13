INF = float('inf')
n, k = map(int, input().split())
L = list(map(int, input().split()))
ans = INF
for i in range(n-k+1):
    r = L[i+k-1]
    l = L[i]
    tr = abs(r) + abs(l - r)
    tl = abs(l) + abs(r - l)
    t = min(tr, tl)
    ans = min(ans, t)
print(ans)
