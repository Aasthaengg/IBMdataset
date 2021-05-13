import sys
input = sys.stdin.readline
R,C,K = map(int,input().split())
RCV = [tuple(map(int,input().split())) for i in range(K)]

goods = [dict() for _ in range(R)]
for r,c,v in RCV:
    r,c = r-1,c-1
    goods[r][c] = v

dp0 = [[0]*4 for _ in range(C)]
dp1 = [[0]*4 for _ in range(C)]
if 0 in goods[0]:
    dp1[0][1] = goods[0][0]
for i in range(R):
    for j in range(C):
        if i:
            pre = max(dp0[j])
            dp1[j][0] = pre
            if j in goods[i]:
                dp1[j][1] = pre + goods[i][j]
        if j:
            for k in range(4):
                dp1[j][k] = max(dp1[j][k], dp1[j-1][k])
            if j in goods[i]:
                for k in reversed(range(3)):
                    dp1[j][k+1] = max(dp1[j][k+1], dp1[j-1][k] + goods[i][j])
    dp0 = dp1
    dp1 = [[0]*4 for _ in range(C)]
print(max(dp0[-1]))