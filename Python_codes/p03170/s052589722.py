import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = tuple(map(int, input().split()))

dp = [None] * (k + k + 1)
# dp[手番の石の数] := 手番の勝敗
# True(勝ち) / None(負け)

for opponent_remains in range(k):  # 自分が石を取った残りなので、k未満
    if dp[opponent_remains] is None:  # 相手が負ける場合
        for my_take in a:  # 自分が取る石の数
            my_remains = opponent_remains + my_take  # 相手が負けるようにできる、自分の手番の石の数
            dp[my_remains] = True

ans = dp[k]
print('First' if ans else 'Second')

# 内側のループに入る前に枝刈りしているので、速い
