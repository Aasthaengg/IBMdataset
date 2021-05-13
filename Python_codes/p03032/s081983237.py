N, K = map(int, input().split())
V = list(map(int, input().split()))

def solve(N,K,V):
    ans = 0
    V = V*2
    for l in range(N+1):
        for r in range(N-1,2*N):
            n = r-l+1
            if n == 0 or n>K or n>N:
                continue
            p = K-n
            W = V[l:r+1]
            W.sort()
            total = sum(W)
            firstp = W[:p]
            for w in firstp:
                if w<0:
                    total -= w
                else:
                    break
            ans = max(ans,total)
    return ans
print(solve(N,K,V))