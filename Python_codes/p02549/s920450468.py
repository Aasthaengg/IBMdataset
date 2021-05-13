import sys
input = sys.stdin.readline
N,K = map(int,input().split())
LR = [tuple(map(int,input().split())) for i in range(K)]
MOD = 998244353

dp = [1]
cumdp = [0,1]
for i in range(1,N):
    tmp = 0
    for l,r in LR:
        if i-l+1 <= 0: continue
        tmp += cumdp[i-l+1] - cumdp[max(0,i-r)]
    tmp %= MOD
    dp.append(tmp)
    cumdp.append((cumdp[-1] + tmp) % MOD)
print(dp[-1])