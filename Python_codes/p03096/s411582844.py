import sys,math,collections,itertools
input = sys.stdin.readline

N = int(input())
ans = 1
m=10**9+7
c=[]
for _ in range(N):
    c.append(int(input()))
dp = [1]*(N+1)#dp[i] i番目までの並び替え総数
last_color = [-1]*(max(c)+1)#最後にその色が出たindexの保存
last_color[c[0]] =0
for i in range(1,N):
    if c[i]==c[i-1]:#同じ色が続くとリバーシできない
        dp[i] = dp[i-1]
    else:
        if last_color[c[i]]==-1:#初めての色はリバーシできない
            dp[i] = dp[i-1]
            last_color[c[i]]=i
        else:#挟める石があるし色が連続してない
            dp[i] = dp[i-1]+dp[last_color[c[i]]]#最後に出た石と挟むか挟まないk
            last_color[c[i]]=i
print(dp[N-1]%m)
