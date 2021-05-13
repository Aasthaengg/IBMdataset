import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

n,m = na()
abc = [tuple(na()) for i in range(m)]

dp = [float('inf')]*n
dp[0] = 0

for i in range(n):
    for a,b,c in abc:
        a,b,c = a-1,b-1,-c
        if dp[a] != float('inf') and dp[b] > dp[a] + c:
            dp[b] = dp[a] + c
            if i == n-1 and b == n-1:
                print('inf')
                exit()

print(-dp[-1])
