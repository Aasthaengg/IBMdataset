def fennec_vs_monster():
    # 入力
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    # 体力リストを降順でソート
    H.sort(reverse=True)
    # 体力リストを先頭からK個だけ除外
    H = H[K:]
    # 残りの体力リストを合計
    sum_H = sum(H)
    # 攻撃の回数の最小値
    return sum_H

result = fennec_vs_monster()
print(result)