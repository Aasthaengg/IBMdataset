from bisect import bisect_left
N,K = map(int,input().split())
V = list(map(int,input().split()))
vmax = -10**9
for n in range(min(N,K)+1):
    A = V[:n]
    for m in range(min(N,K)-n+1):
        B = V[N-m:]
        B = B+A
        B = sorted(B)
        ind = bisect_left(B,0)
        k = min(ind,K-n-m)
        v = sum(B[k:])
        vmax = max(vmax,v)
print(vmax)       