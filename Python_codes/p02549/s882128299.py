N, K = map(int, input().split())
LRs = [tuple(map(int, input().split())) for _ in range(K)]
mod = 998244353

def diff(l):
    tmp = None
    res = []
    for elm in l:
        if tmp is None:
            res.append(elm)
            tmp = elm
        else:
            res.append(elm-tmp)
            tmp = elm

    return res

res_diff = [0] * N
res_diff[1] = -1
res = [1]

for i in range(N-1):
    for l, r in LRs:
        if i+l < N:
            res_diff[i+l] += res[i]
        if i+r+1 < N:
            res_diff[i+r+1] -= res[i]
    
    res_next = (res[-1]+res_diff[i+1])%mod
    res.append(res_next)

print(res[N-1])