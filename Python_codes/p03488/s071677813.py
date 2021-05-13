S = input()
gx, gy = map(int, input().split())
SL = S.split('T')
D = [len(sli) for sli in SL]
DX = D[2::2]
DY = D[1::2]

def reachable(D, s, g):
    dp = [{} for _ in range(len(D)+1)]
    dp[0][s] = 1
    for i in range(len(D)):
        d = D[i]
        for j in dp[i]:
            dp[i+1][j+d] = 1
            dp[i+1][j-d] = 1
    return g in dp[-1]

if reachable(DX, D[0], gx) and reachable(DY, 0, gy):
    print('Yes')
else:
    print('No')
