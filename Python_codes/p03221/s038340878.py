"""
M <= 10 ** 5
なので全探索しても間に合いそう。
"""
N, M = map(int, input().split())
input_li = []   # 入力[p, y]の組み合わせを格納する二次元リスト
p_dict = {}     # pごとのyのリストを格納する辞書
ans_dict = {}   # キーp, yを指定することでIDが取り出せる辞書

# 入力をinput_liに詰めつつp_dictを作っていく
for _ in range(M):
    p, y = map(int, input().split())
    input_li.append([p, y])
    if p not in p_dict:
        li = [y]
        p_dict[p] = li
    else:
        p_dict[p].append(y)

# p_dictを元にans_dictを作っていく
for p in p_dict:
    li = sorted(p_dict[p])
    ans_dict[p] = {}
    for i in range(len(li)):
        p_id = '0' * (6 - len(str(p))) + str(p)
        c_id = '0' * (6 - len(str(i + 1))) + str(i + 1)
        ans_dict[p][li[i]] = p_id + c_id

# input_li順にIDを出力していく
for p, y in input_li:
    print(ans_dict[p][y])
