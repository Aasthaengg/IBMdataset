s = input()
# list関数を使う
n = len(s)
list_s = list(s)
list_s_part1 = list_s[0:(n - 1) // 2]
list_s_part2 = list_s[(n + 1) // 2:n]
# 各種listを逆順に並び替える
list_s_rev = list(reversed(list_s))
list_s_part1_rev = list(reversed(list_s_part1))
list_s_part2_rev = list(reversed(list_s_part2))
if ''.join(list_s) == ''.join(list_s_rev) and\
    ''.join(list_s_part1) == ''.join(list_s_part1_rev) and\
    ''.join(list_s_part2) == ''.join(list_s_part2_rev):
    print('Yes')
else: print('No')