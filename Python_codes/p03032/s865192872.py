from bisect import bisect_left as bil
N, K, *V = map(int, open(0).read().split())


k = min(N, K)
ans = 0
for i in range(k+1):
    for j in range(k-i+1):
        U = V[:i]+V[-j:] if j != 0 else V[:i]
        U.sort()
        z = min(bil(U, 0), K-i-j)
        sm = sum(U[z:])

        if ans < sm:
            ans = sm

print(ans)
