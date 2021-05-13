import sys

inp = [int(x) for x in sys.stdin.read().split()]
ii = 0

r, c, k = inp[ii:ii+3]
ii += 3
v=[0] * (c * r)
for _ in range(k):
    ri,ci,a = inp[ii:ii+3]
    ii += 3
    v[(ri-1)*c + (ci-1)]=a
dp= [0] * (c * r * 4)
x = c * r
if v[0]>0: dp[x] = v[0]

for i in range(r):
    for j in range(c):
        idx = i*c+j
        idx2 = (i-1)*c + j
        idx3 = i*c + j-1
        val = v[idx]
        if i>0:
            a = max(dp[idx2],dp[x + idx2],dp[2*x+idx2],dp[3*x+idx2])
            dp[idx]= a
            dp[x+idx]= a + val

        if j>0:
            dp[idx]=max(dp[idx],dp[idx3])
            dp[x + idx]=max(dp[x + idx],dp[idx3]+val,dp[x + idx3])
            dp[2*x + idx]=max(dp[x+idx3]+val,dp[2*x+idx3])
            dp[3*x + idx]=max(dp[2*x+idx3]+val,dp[3*x+idx3])


ans=0
for i in range(4): ans = max(dp[i*x + (r-1)*c + (c-1)],ans)
print(ans)

