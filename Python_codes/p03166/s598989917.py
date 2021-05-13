import sys
sys.setrecursionlimit(10**6)
N, M = list(map(int, input().split()))
P = [set() for _ in range(N)]
for i in range(M):
    x, y = list(map(int, input().split()))
    x -= 1
    y -= 1
    P[x].add(y)

dp = [-1]*N


def lpth(n):
    if dp[n] > -1:
        return dp[n]
    l = P[n]
    # print(l)
    if l:
        s = [lpth(k) for k in l]
        # print(s)
        a = max(s)+1
    else:
        a = 0
    dp[n] = a
    return a


for i in range(N):
    dp[i] = lpth(i)
print(max(dp))
# print(dp)
