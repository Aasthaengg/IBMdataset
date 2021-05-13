n, k = map(int, input().split())
lst = list(map(int, input().split()))

dp = [0] * (k+1) #dp[i]は石の数が残りi個のときに手番プレイヤーが勝利できるか

for i in range(1, k+1):
    flg = 0
    for j in lst:
        if i - j >= 0:
            if not dp[i-j]: #一度でも0(False)があればflg1(True)
                flg = 1
                break
    if flg:
        dp[i] = 1
            
if dp[k]:
    print('First')
else:
    print('Second')