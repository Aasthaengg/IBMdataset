def duplex_printing(all_pages):
    # 集計
    all_papers = (all_pages + 1) // 2
    # 戻り値
    return all_papers

# 入力
N = int(input())
# 関数処理
result = duplex_printing(N)
# 表示
print(result)