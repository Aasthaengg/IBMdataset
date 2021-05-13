N, K = map(int,input().split())
R, S, P = map(int,input().split())
T = input()
# 相手の手に対して勝ったときの得点
rsp_dic = {"r":P,"s":R,"p":S}
# 相手の手に対して
rsp_dic2 = {0:P,1:R,2:S}
# 自分の手に対して勝てる相手の手
rsp_win = ["s","p","r"]
# 相手の手に対して勝てる自分の手
rsp_lose = {"r":2,"s":0,"p":1}

anslist = [0] * K

modcount = [N//K]*K
for i in range(1,N%K+1):
    modcount[i] += 1

for k in range(K):
    count = modcount[k]
    dp = [[0,0,0] for _ in range(count+1)]
    for i in range(1, count+1):
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1])
        if k != 0:
            dp[i][rsp_lose[T[(i-1) * K + k - 1]]] += rsp_dic[T[(i-1) * K + k - 1]]
        else:
            dp[i][rsp_lose[T[i * K + k - 1]]] += rsp_dic[T[i * K + k - 1]]

    anslist[k] = max(dp[-1])

print(sum(anslist))