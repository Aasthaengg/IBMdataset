import sys
readline = sys.stdin.readline

N,K = map(int,readline().split())
A = list(map(int,readline().split()))

# dp[i] = 石の残り数がiの時の勝敗
# i個の状態から遷移できる場所に負けが存在したら、それを相手に回すことが出来るため勝ち
# i個の状態から遷移できる場所に勝ちが存在したら、それを相手に回す必要はないので更新なし

dp = [False] * (K + 1)
for i in range(1, K + 1): # 石がi個の状態
  for j in range(len(A)): # それを相手に回す元が存在するかチェック
    if i - A[j] >= 0 and not dp[i -A[j]]:
      dp[i] = True

print(("Second","First")[dp[K]])  