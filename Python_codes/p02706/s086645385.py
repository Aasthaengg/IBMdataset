# 問題文
# 高橋君の夏休みはN日間です。
# 夏休みの宿題が M個出されており、i番目の宿題をやるにはAi日間かかります。
# 複数の宿題を同じ日にやることはできず、また、宿題をやる日には遊ぶことができません。
# 夏休み中に全ての宿題を終わらせるとき、最大何日間遊ぶことができますか？
# ただし、夏休み中に全ての宿題を終わらせることができないときは、かわりに -1 を出力してください。

# n（夏休みの日数）,m（宿題の数）：標準入力
# リストの中のA(宿題日)：リストを作成し、標準入力
n, m = map(int, input().split())
A = list(map(int, input(). split()))

# 最大で n −合計(A1+. . .+AM)日間遊ぶことができる
if n < sum(A):   # 夏休みの日数より宿題日が多い場合：宿題をやる日数が足りない→終わらせることができない
    print(-1)
else:
    print(n-sum(A)) # その他→宿題は終わる→夏休みの日数-宿題日

# NameError: name 'N' is not defined