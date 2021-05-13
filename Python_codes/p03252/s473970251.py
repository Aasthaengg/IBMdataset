"""
S = chokudai
T = redcoder

'redcoder' には 'e' が２つあるので一度に変える必要があるが、
Sではそれに相当する場所には 'h' と 'a' の2種類の文字があるので不可能。
こういう感じで一文字ずつ見ていけばよさそう。

10 ** 5なのでstring.count()とか使っちゃうとTLEしそう。

文字の出現回数を格納するリストを作っていって、それぞれ比較すればよさそう。
上の例だと、
    s_li = [1, 1, 1, 1, 1, 1, 1, 1]
    t_li = [2, 2, 2, 1, 1, 2, 2, 2]
になり、s_liとt_liの中身が異なるのでNG。
"""
from collections import defaultdict

S = input()
T = input()
s_li = [0] * len(S)   # 文字列Sに登場する文字の出現回数を順番に格納する
t_li = [0] * len(T)   # 文字列Tに登場する文字の出現回数を順番に格納する

# s_liを作っていく
s_cnt_dict = defaultdict(int)   # 文字ごとに出現回数をメモしていく
s_idx_dict = defaultdict(list)  # 同じ文字が出現するインデックスをメモしていく
for i in range(len(S)):
    k = S[i]
    s_cnt_dict[k] += 1
    s_idx_dict[k].append(i)
for k in s_cnt_dict:
    for idx in s_idx_dict[k]:
        s_li[idx] = s_cnt_dict[k]

# t_liを作っていく
t_cnt_dict = defaultdict(int)   # 文字ごとに出現回数をメモしていく
t_idx_dict = defaultdict(list)  # 同じ文字が出現するインデックスをメモしていく
for i in range(len(T)):
    k = T[i]
    t_cnt_dict[k] += 1
    t_idx_dict[k].append(i)
for k in t_cnt_dict:
    for idx in t_idx_dict[k]:
        t_li[idx] = t_cnt_dict[k]

print('Yes') if s_li == t_li else print('No')
