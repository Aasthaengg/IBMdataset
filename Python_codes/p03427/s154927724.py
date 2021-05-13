import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    n = int(input())
    k = len(str(n))
    dp = [0, -INF]

    for c in str(n):
        c = int(c)
        ndp = [-INF, -INF]
        for d in range(10):
            for lt in range(2):
                if not lt and c < d:
                    continue
                nlt = max(lt, c > d)
                ndp[nlt] = max(ndp[nlt], dp[lt] + d)
        dp = ndp

    print(max(dp))
resolve()