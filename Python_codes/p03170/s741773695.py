n, k = map(int, input().split())
a = tuple(map(int, input().split()))

#dp[i] := 残りがi個の時に手番が回ってきた方の勝敗
#0: 負け,
#1: 勝ち
#当然残り0個は負け
dp = [0] * (k+1)
#aの要素だけ残っている時，それを全てとってしまい，相手に0を渡すことができるので，1になる
for i in a:
    dp[i] = 1

#数字が小さい方からチェックしていき，aのいずれかの要素だけ小さくなったとき勝ちなら勝ち
#そうでなければ負け
for i in range(1, k+1):
    for e in a:
        #まず取れないとダメ
        if i > e:
            #その上で遷移後の状態を調べる
            if not dp[i-e]:
                dp[i] = 1

if dp[k]:
    print("First")
else:
    print("Second")