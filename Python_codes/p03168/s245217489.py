
N = int(input())

fac = [1]
for i in range(N):
    i += 1
    fac.append(fac[-1] * i)

def nCr(n,r):
    return fac[n] // (fac[r] * fac(n-r))

p = list(map(float,input().split()))

"""

dpだよな
表と裏がa,N-a枚となる確率は？
無理かなぁ

左から見ていってdp?
表がa枚になる確率は p*(a-1枚の確率) + (1-p)*(a枚の確率)
→いけそう

"""

dp = [0] * (N+1)
dp[0] = 1

for loop in range(N):

    ndp = [0] * (N+1)

    for i in range(N):

        ndp[i+1] += dp[i] * p[loop]
        ndp[i] += dp[i] * (1-p[loop])

    dp = ndp

ans = 0
for i in range(N+1):
    if i > N-i:
        ans += dp[i]

print (ans)
