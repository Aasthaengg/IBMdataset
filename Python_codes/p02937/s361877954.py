"""
tの先頭から、できるだけ長い文字列を一回のsで消費するゲーム
できるだけ短い時間で、残っているtの先頭からどこまでを一回で消費できるかを判断したい。
部分文字列DPのときにやったみたいに、ns[i][j] => i番目より後ろで、つぎに文字jが出てくるインデックス
という表を作っておけばよい。
"""

S = input()
T = input()
N = len(S)
dp = [[-1]*26 for _ in range(N+1)]
for i in range(N):
    s = S[i]
    dp[i][ord(s)-ord("a")] = i+1

for i in range(N-2,-1,-1):
    for j in range(26):
        if dp[i][j] == -1:
            dp[i][j] = dp[i+1][j]

cycleCnt = 0
sInd = 0
for i in range(len(T)):
    if dp[sInd][ord(T[i])-ord("a")] == -1:
        cycleCnt += 1
        sInd = 0
        if dp[sInd][ord(T[i])-ord("a")] == -1:
            print(-1)
            exit()
    sInd = dp[sInd][ord(T[i])-ord("a")]
else:
    print(cycleCnt*N+sInd)

