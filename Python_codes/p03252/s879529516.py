# 基本的には一文字ずつ変えていけば変わるはずだがある一つの文字に複数の別の文字が当たってると変換できない
# chokudai
# redkuoai
# redcouai
# reucodai
# raucodei
# iaucoder

S = list(input())
T = list(input())

from collections import defaultdict
s_dic = defaultdict(set)
t_dic = defaultdict(set)
for i in range(len(S)):
    s = S[i]
    t = T[i]
    if len(s_dic[s]) > 0 and t not in s_dic[s]:
        print('No')
        exit()
    if len(t_dic[t]) > 0 and s not in t_dic[t]:
        print('No')
        exit()
    s_dic[s].add(t)
    t_dic[t].add(s)

print('Yes')
