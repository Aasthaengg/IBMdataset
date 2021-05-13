import bisect

N, K = map(int, input().split())
V = [int(i) for i in input().split()]

ans = -10**20
for l in range(min(K+1, N+1)):
    for r in range(min(K-l+1, N-l+1)):
        P = V[:l]+V[N-r:]
        P.sort()
        z = bisect.bisect_left(P, 0)

        if z <= K-l-r:
            ans = max(ans, sum(P[z:]))
        else:
            ans = max(ans, sum(P[K-l-r:]))

print(ans)
