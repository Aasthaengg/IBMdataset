import sys,heapq
input = sys.stdin.buffer.readline
 
R,C,k = map(int,input().split())
 
 
val = dict()
for _ in range(k):
    rr,cc,vv = map(int,input().split())
    rr -= 1
    cc -= 1
    val[rr*C + cc] = vv
 
dp = [[0,0,0,0] for i in range(C)]
dp2 = [[0,0,0,0] for i in range(C)]

for i in range(R):
    for j in range(C):
        idx  = j
        if i*C + j in val:
            v = val[i*C + j]
        else:
            v = 0
        if i%2 == 0:
            if i == 0:
                if j == 0:
                    dp[idx][1] = v
                else:
                    dp[idx][1] = max(dp[idx-1][1],v)
                    dp[idx][2] = max(dp[idx-1][2],dp[idx-1][1] + v)
                    dp[idx][3] = max(dp[idx-1][3],dp[idx-1][2] + v)
            else:
                if j == 0:
                    dp[idx][0] = max(dp2[idx][0],dp2[idx][1],dp2[idx][2],dp2[idx][3])
                    dp[idx][1] = dp[idx][0] + v
                else:
                    dp[idx][0] = max(dp2[idx][0],dp2[idx][1],dp2[idx][2],dp2[idx][3],dp[idx-1][0])
                    dp[idx][1] = max(dp[idx-1][1],dp[idx][0] + v)
                    dp[idx][2] = max(dp[idx-1][2],dp[idx-1][1] + v)
                    dp[idx][3] = max(dp[idx-1][3],dp[idx-1][2] + v)
        else:
            if i == 0:
                if j == 0:
                    dp2[idx][1] = v
                else:
                    dp2[idx][1] = max(dp2[idx-1][1],v)
                    dp2[idx][2] = max(dp2[idx-1][2],dp2[idx-1][1] + v)
                    dp2[idx][3] = max(dp2[idx-1][3],dp2[idx-1][2] + v)
            else:
                if j == 0:
                    dp2[idx][0] = max(dp[idx][0],dp[idx][1],dp[idx][2],dp[idx][3])
                    dp2[idx][1] = dp2[idx][0] + v
                else:
                    dp2[idx][0] = max(dp[idx][0],dp[idx][1],dp[idx][2],dp[idx][3],dp2[idx-1][0])
                    dp2[idx][1] = max(dp2[idx-1][1],dp2[idx][0] + v)
                    dp2[idx][2] = max(dp2[idx-1][2],dp2[idx-1][1] + v)
                    dp2[idx][3] = max(dp2[idx-1][3],dp2[idx-1][2] + v)
 
print(max(max(dp[-1]),max(dp2[-1])))