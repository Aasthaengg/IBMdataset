H, W = map(int, input().split())
S = [0]*(H+1)
S[0] = '*'*(W+1)
for h in range(1,H+1):
    S[h] = '*' + input()

dps = [[0]*(W+1) for _ in range(H+1)]
mod = 10**9+7

def dp(h,w):
    if h==1 and w==1:
        return 1
    if S[h][w]=='.':
        return (dps[h-1][w]+dps[h][w-1])%mod
    return 0


def solve():
    for h in range(1,H+1):
        for w in range(1,W+1):
            dps[h][w] = dp(h,w)
    ans = dps[-1][-1]
    return ans
print(solve()) 