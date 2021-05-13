import sys

def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし

N = [0] + LI2()
n = len(N)

dp1 = [0]*(n)
dp2 = [0]*(n)

# Nを N_1N_2…N_(n-1) と表す
# またf(a)をa円払うときの自分と店員が使う紙幣の枚数の和の最小値とする
# このとき、f(N_1…N_k) = min(f(N_1…N_(k-1))+N_k,f(N_1…(N_(k-1)+1))+10-N_k) が成立する
# ここで、dp1[i] = f(N_1…N_i),dp2[i] = f(N_1…(N_i+1)) と定めdpする

for i in range(n):
    if i == 0:
        dp2[i] = 1
    else:
        dp1[i] = min(dp1[i-1]+N[i],dp2[i-1]+10-N[i])
        dp2[i] = min(dp1[i-1]+N[i]+1,dp2[i-1]+9-N[i])

print(dp1[n-1])