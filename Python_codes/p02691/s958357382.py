from collections import defaultdict
n = int(input())
L_dict, R_dict = defaultdict(int), defaultdict(int)
i = 0
for ipt in input().split():
    L_dict[i + int(ipt)] += 1
    R_dict[i - int(ipt)] += 1
    i += 1
cnt = 0
for Lk, Lv in L_dict.items():
        cnt += R_dict[Lk] * Lv
print(cnt)