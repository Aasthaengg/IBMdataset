# D - We Like AGC

import itertools, copy

N = int(input())
MOD = 10**9+7

if N == 3:
    print(4**3-3)
    exit()

# AGCそれ自体を含むか、1箇所入れ替えてAGCができてしまうような4文字
out_letters_4 = set()
for x in ["A", "C", "G", "T"]:
    out_letters_4.add("A" + x + "GC")
    out_letters_4.add("AG" + x + "C")
    for y in ["AGC", "GAC", "ACG"]:
        out_letters_4.add(x + y)
        out_letters_4.add(y + x)

# 全4文字辞書
tmp = list(itertools.product(["A", "C", "G", "T"], repeat = 4))
all_letters_4 = set()
for x in tmp:
    tmp2 = ""
    for y in x:
        tmp2 += y
    all_letters_4.add(tmp2)

possible_letters_4 = all_letters_4 - out_letters_4

# 文字を末尾に追加する前の末尾の4文字(key)、文字追加後の末尾の4文字(value)の辞書
trans_letters_4_dict = dict.fromkeys(possible_letters_4, -1)
for key in trans_letters_4_dict.keys():
    for x in ["A", "C", "G", "T"]:
        tmp = (key + x)[1:]
        if tmp in trans_letters_4_dict.keys():
            if trans_letters_4_dict[key] == -1:
                trans_letters_4_dict[key] = [tmp]
            else:
                trans_letters_4_dict[key].append(tmp)

n_pattern = dict.fromkeys(possible_letters_4, 1)

for _ in range(N-4):
    next_n_pattern = dict.fromkeys(possible_letters_4, 0)
    for former_key in possible_letters_4:
        for to_key in trans_letters_4_dict[former_key]:
            next_n_pattern[to_key] += n_pattern[former_key]
    n_pattern = copy.deepcopy(next_n_pattern)

print(sum(n_pattern.values()) % MOD)