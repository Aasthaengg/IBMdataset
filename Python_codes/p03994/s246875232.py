# https://atcoder.jp/contests/code-festival-2016-quala/tasks/codefestival_2016_qualA_c
# 辞書最小にしたい
# 前から貪欲 (OK)
# 実装が分からない

from bisect import bisect_left
from string import ascii_lowercase

s = input()
k = int(input())

ac = list(ascii_lowercase) + ['a']
dmap = {}
for i in range(len(ac) - 1):
    # dmap[ac[i]] = min(i, len(ac) - i - 1)
    dmap[ac[i]] = len(ac) - i - 1
dmap['a'] = 0

ans = list(s)
output = []

for idc, c in enumerate(ans):
    if k >= dmap[c]:
        output.append('a')
        k -= dmap[c]
    else:
        output.append(c)

k %= 26
# 最後に残ったkをすすめる
new_char = chr(ord(output[-1]) + k)
output[-1] = new_char
print("".join(output))