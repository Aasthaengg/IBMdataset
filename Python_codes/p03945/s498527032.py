# BWBWB と BWWBBBBWWWWWWBBBBB を一色にする手順は同じ。
from itertools import groupby

S = input()
grp = [k for k, _ in groupby(S)]
print(len(grp) - 1)
