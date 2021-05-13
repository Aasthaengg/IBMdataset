N = int(input())
L = []
for i in range(N):
    L.append(list(map(int, input().split())))
# print(L)

# その日までの幸福度の最大, ではデータが不足
# ∵翌日何の行動がとれるかわからないから
# dp[i][j]:i+1日目に行動jをしたときの幸福度最大値

dp=[[0,0,0] for i in range(N)]
for j in range(3):
    dp[0][j]=L[0][j]
# print(dp)

for i in range(1,N):
    for j in range(3):
        for k in range(3):
            if j != k:
                dp[i][j]=max(dp[i][j], dp[i-1][k] + L[i][j])
    # print(dp[i])
print(max(dp[N-1]))