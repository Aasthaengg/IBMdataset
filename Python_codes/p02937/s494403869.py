from collections import defaultdict
import bisect

S = list(str(input()))
T = list(str(input()))

dict = defaultdict(list)
for i, c in enumerate(S):
    dict[c].append(i + 1)
# print(dict)

# Sの繰り返し数
div_cnt = 0
# 現在のindex
now = 0

for i, c in enumerate(T):

    # cがS中に存在しない場合
    if dict[c] == []:
        print(-1)
        exit()

    next = bisect.bisect_right(dict[c], now)
    # print(c, now, next)

    # nextがdictの右端になる場合
    # 次のsブロックを使う
    if next == len(dict[c]):
        div_cnt += 1
        now = dict[c][0]
    # 現在のsブロックがまだ使える場合
    else:
        now = dict[c][next]

ans = div_cnt * len(S) + now
print(ans)
