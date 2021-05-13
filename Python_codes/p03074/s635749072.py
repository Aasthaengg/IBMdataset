import sys
input = sys.stdin.readline

from itertools import groupby

N, K = [int(x) for x in input().split()]
S = list(input().rstrip())

S_groupby = groupby(S)

zero_idx = [] # ゼロが何番目か
value_list = [] # 各インデックスのキーに対する個数
i = -1
for j in S_groupby:
    i += 1
    key, value = j[0], len(list(j[1]))
    value_list.append(value)
    if key == '0':
        zero_idx.append(i)

if len(zero_idx) <= K:
    print(len(S))
    sys.exit()

left = zero_idx[0]
right = zero_idx[K - 1]
if zero_idx[0] == 0:
    ans = [sum(value_list[left:right + 2])]
else:
    ans = [sum(value_list[left - 1:right + 2])]

for i in range(K, len(zero_idx)):
    new_right = zero_idx[i]
    new_left = zero_idx[i - K + 1]
    new_ans = ans[-1] + value_list[new_right] - value_list[left]
    if new_right + 1 < len(value_list):
        new_ans += value_list[new_right + 1]
    if left - 1 >= 0:
        new_ans -= value_list[left - 1]
    ans.append(new_ans)
    right, left = new_right, new_left

print(max(ans))
