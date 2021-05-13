# coding: utf-8
# Your code here!

# 最大積載量p でk台のトラックに全ての荷物を積載できるかチェックする
def check(p):
  global n, k, w

  # k台のトラックに積載済の荷物の個数
  i = 0

  # k台のトラックに順番に荷物を積載する
  for j in range(k):
    # j台目のトラックの積載量の合計
    s = 0

    # 積載量の合計が 最大積載量p を超えるまで荷物を積み込む
    while (s + w[i] <= p):
      s += w[i]
      
      # トラックに積載済の荷物の個数をカウントアップ
      i += 1

      # 最大積載量p で すべての荷物を積み込めた場合
      if (i == n):
        return True

  # 最大積載量p で すべての荷物を積み込めなかった場合
  return False


# メイン処理
def solve():
  global n

  # 積載量の下限
  left = 0

  # 積載量の上限（個数の最大値 × 重量の最大値）
  right = 100000 * 10000

  while (1 < right - left):
    # 最大積載量p
    p = int((left + right) / 2)

    if check(p):
      # 最大積載量pで全ての荷物が積み込めた場合、p より小さい範囲を探索
      right = p
    else:
      # 最大積載量pで全ての荷物が積み込めなかった場合、p より大きい範囲を探索
      left = p
  
  # 全ての荷物を積み込むことができた最小の最大積載量を返却する
  return right

n, k = map(int, input().split())
w = [int(input()) for i in range(n)]
print(solve())
