import collections

def poll():
    # 入力
    N = int(input())
    S = list()
    for _ in range(N):
        S.append(input())
    # 各文字列の出現回数をカウント
    count_list = collections.Counter(S)
    # 最大の出現回数のvalueのみ抽出
    max_count = max(count_list.values())
    max_count_str = list()
    for key, value in count_list.items():
        if value == max_count:
            max_count_str.append(key)
    # ソート
    return sorted(max_count_str)
           
result = poll()
for string in result:
    print(string)