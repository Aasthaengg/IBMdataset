K, A, B = map(int, input().split())
CNT = K - A + 1     # 最初、A枚になるまでビスケットを増やす
# 残り回数でできるだけAとBを行う
# 残り回数が1余ったならビスケットを増やす
print(max(A + CNT // 2 * (B - A) + CNT % 2, K + 1))