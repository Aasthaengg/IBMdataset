n = int(input())
A = list(map(int, input().split()))
ans = float('inf')
# 各Aiを見ていく時 iが奇数、偶数どちらの時の和を負の数にするか
for case in range(2):
    count = 0  # 操作回数
    sum_a = 0  # Ai までの数の和
    up = case  # 和を正整数にするか
    for a in A:
        sum_a += a
        diff = 0  # a をどの程度操作するか。
        if up:  # 正整数であるべき
            if sum_a < 1:  # 1未満の数(0か負数)
                diff = 1 - sum_a
        else:  # 負整数であるべき
            if -1 < sum_a:  # -1より大きい数(0か正整数)
                diff = -1 - sum_a
        sum_a += diff  # Ai までの和に操作後の値を適用する
        count += abs(diff)  # 操作回数を加算する
        up ^= 1  # 次回は今回とは逆の符号にする
    ans = min(count, ans)  # 最小操作回数を更新
print(ans)
