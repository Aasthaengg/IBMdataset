def li():
    return [int(x) for x in input().split()]


N = int(input())
L = []
for i in range(N):
    L.append(li())

# 1.全探索は間に合うか: 再帰で全探索するとO(3**N)で間に合わない
# 2.貪欲法は使えるか: 一手での最善(部分最適)は次の一手の大きなメリットを逃す可能性があルため最善ではない
# 3.DPは使えるか: 一手ごとにA,B,Cの状態別に最大値1つだけに注目すれば良く、残りは切り捨てて良いので使える

# dp[i][k]: i番目の選択でk(a,b,c)を選択した時の最大値
dp = [[0]*3 for i in range(N+1)]
dp[0] = L[0]
for i in range(1, N):
    for k in range(3):
        if k == 0:
            dp[i][k] = max(dp[i][k], dp[i-1][1] + L[i][0], dp[i-1][2] + L[i][0])
        elif k == 1:
            dp[i][k] = max(dp[i][k], dp[i-1][0] + L[i][1], dp[i-1][2] + L[i][1])
        elif k == 2:
            dp[i][k] = max(dp[i][k], dp[i-1][0] + L[i][2], dp[i-1][1] + L[i][2])

print(max(dp[N-1]))