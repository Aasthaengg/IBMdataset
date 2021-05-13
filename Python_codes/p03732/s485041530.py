from collections import defaultdict
N,W = map(int,input().split())
wv = [list(map(int,input().split())) for _ in range(N)]
w1 = wv[0][0]
ws = []
ijkl = [0,0,0,0]
for i in range(N):
    w = wv[i][0]
    ijkl[w-w1] += 1
for i in range(ijkl[0]+1):
    for j in range(ijkl[1]+1):
        for k in range(ijkl[2]+1):
            for l in range(ijkl[3]+1):
                w = i*w1+j*(w1+1)+k*(w1+2)+l*(w1+3)
                if w <= W:
                    ws.append(w)
ws = list(set(ws))
ws.sort()
dp = [defaultdict(lambda:-float('inf')) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    for j in ws:
        w,v = wv[i]
        dp[i+1][j] = max(dp[i][j],dp[i][j-w]+v)
print(max(dp[N].values()))