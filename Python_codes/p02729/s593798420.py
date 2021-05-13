"""
偶数：偶数＋偶数 or 奇数＋奇数
奇数：偶数＋奇数
"""

def the_number_of_even_pairs():
    # 入力
    N, M = map(int, input().split())
    # 初期処理
    list_N = [0] * N
    list_M = [1] * M
    even_pairs_count = 0
    # 判別処理
    # 偶数＋偶数
    for _ in range(N):
        even_pairs_count += len(list_N)-1
        list_N.pop(0)
    # 奇数＋奇数
    for _ in range(M):
        even_pairs_count += len(list_M)-1
        list_M.pop(0)
    # 結果
    return even_pairs_count

result = the_number_of_even_pairs()
print(result)