import bisect
N,K= map(int,input().split())
V = list(map(int,input().split()))
sortedV = sorted(V)
rV = V[::-1]

ans = -10**10
for nout in range(K+1):
    nin = K-nout
    if nout >= N:
        cand = sortedV
        ind = bisect.bisect_left(cand,0)
        ind = min(ind,nin)
        ans = max(ans, sum(cand[ind:]))
    else:
        for nleft in range(nout+1):
            nright = nout - nleft
            cand = V[:nleft] + rV[:nright]
            cand.sort()
            ind = bisect.bisect_left(cand,0)
            ind = min(ind,nin)
            ans = max(ans, sum(cand[ind:]))
print(ans)




