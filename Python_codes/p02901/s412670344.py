import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ks = []

for _ in range(M):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    T = 0
    
    for ci in c:
        T += 1<<(ci-1)
    
    ks.append((a, T))

dp = [10**18]*(1<<N)
dp[0] = 0

for S in range(1<<N):
    for a, T in ks:
        dp[S|T] = min(dp[S|T], dp[S]+a)

if dp[-1]==10**18:
    print(-1)
else:
    print(dp[-1])