'''
問題：
    高橋君の夏休みは N 日間です。
    夏休みの宿題が M 個出されており、i 番目の宿題をやるには Ai 日間かかります。

    複数の宿題を同じ日にやることはできず、また、宿題をやる日には遊ぶことができません。
    夏休み中に全ての宿題を終わらせるとき、最大何日間遊ぶことができますか？
    ただし、夏休み中に全ての宿題を終わらせることができないときは、かわりに -1 を出力してください。
'''

'''
制約：
    1 ≦ N ≦ 1000000
    1 ≦ M ≦ 10000
    1 ≦ Ai ≦ 10000
'''

# 標準入力からN, M, Ai を取得する
n, m = map(int, input().split())
a = list(map(int, input().split()))

# 宿題にかかる日数を計算する
work_days = 0
for i in range(0, m):
    work_days += a[i]

# 遊べる日を計算して出力する
result = 0
if n >= work_days:
    result = n - work_days
else:
    result = -1

print(result)
