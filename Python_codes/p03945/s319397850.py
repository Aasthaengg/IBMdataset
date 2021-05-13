s = input()

# 圧縮した文字列 t に対して len(t) - 1 が答え

from itertools import groupby

groups = []
uniquekeys = []
for k, g in groupby(s):
    groups.append(list(g))
    uniquekeys.append(k)

# print(groups)
# print(uniquekeys)

print(len(uniquekeys) - 1)