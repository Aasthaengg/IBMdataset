from bisect import bisect_left
from collections import defaultdict
d = defaultdict(list)

S = input()
T = input()

# 文字列の各文字がどのインデックスにあるか辞書化する
for i in range(len(S)):
    d[S[i]].append(i)


NoFind = False

sequence = 1  # 文字列の連続数
index = -1
for i in range(len(T)):
    if len(d[T[i]]) == 0:
        NoFind = True
        break
    find = bisect_left(d[T[i]], index)
    if find != len(d[T[i]]):
        index = d[T[i]][find] + 1
    else:  # 見つからなかったので文字列を追加
        sequence += 1
        index = -1
        find = bisect_left(d[T[i]], index)
        index = d[T[i]][find] + 1 
            
if NoFind:
    print(-1)
else:
    print(len(S)*(sequence-1) + index)