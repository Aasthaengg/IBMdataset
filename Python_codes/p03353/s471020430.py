S = input()
K = int(input())

import collections
S_count = collections.Counter(S)

ans_list = set()

for key in S_count:
    for idx, s in enumerate(S):
        if s == key:
            short_S = S[idx:min(idx+5, len(S))]
            append_s = ""
            for s in short_S:
                append_s += s
                ans_list.add(append_s)
    if len(ans_list) >= 5:
        break
# print(ans_list)
ans_list = sorted(list(ans_list))
print(ans_list[K-1])