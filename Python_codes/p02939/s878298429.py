import sys

def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

S = LS2()
s = len(S)

dp1 = [0]*s
dp2 = [0]*s
# dp1[i] = 左からi番目までの文字列に対する'K'(但し最後は1文字で分割) 0-index
# dp2[i] = 左からi番目までの文字列に対する'K'(但し最後は2文字で分割) 0-index

for i in range(s):
    if i == 0:
        dp1[i] = 1
        dp2[i] = 0
    elif i == 1:
        if S[i] == S[i-1]:
            dp1[i] = 0
            dp2[i] = 1
        else:
            dp1[i] = 2
            dp2[i] = 0
    else:
        if i >= 3 and S[i-3] == S[i-1] and S[i-2] == S[i]:
            dp2[i] = dp1[i-2]+1
        else:
            dp2[i] = max(dp1[i-2],dp2[i-2])+1

        if S[i] == S[i-1]:
            dp1[i] = dp2[i-1]+1
        else:
            dp1[i] = max(dp1[i-1],dp2[i-1])+1


print(max(dp1[s-1],dp2[s-1]))