from itertools import permutations
n,ma, mb = map(int, input().split())
abc = []
inf = float('INF')
hw = 400 + 1
dp = [[inf for i in range(hw)] for j in range(hw)]
dp[0][0] = 0
for _ in range(n):
    a,b,c = map(int, input().split())
    abc.append((a,b,c))

abc.sort(key = lambda x:(-x[0],x[1]))
for a,b,c in abc:
    for i in range(hw-a)[::-1]:
        for j in range(hw-b)[::-1]:
            if dp[i+a][j+b] > dp[i][j] + c:
                dp[i+a][j+b] = dp[i][j] + c

a,b = ma, mb
ans = [dp[a*i][b*i] for i in range(1,hw // max(a,b)) if dp[a*i][b*i] < inf]
print(min(ans) if len(ans) else -1)
# [print(i, f) for i,f in enumerate(dp[200:])]
# print(ans)