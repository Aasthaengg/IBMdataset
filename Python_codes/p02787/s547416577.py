from sys import stdin


def rec_z():
    for i in range(N):
        for j in range(Hmax+1):
            if j >= a[i]:
                dp[j] = min(dp[j], dp[j-a[i]] + b[i])
    return min(dp[H:Hmax+1])
 
 
readline=stdin.readline
H, N = map(int,readline().split())
a = []
b = []
for i in range(N):
    aa, bb = map(int, readline().split())
    a.append(aa)
    b.append(bb)
Hmax = H + max(a)
INF = 10**9
dp = [INF for _ in range(Hmax+1)] 
dp[0] = 0
print(rec_z())
