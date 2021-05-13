from collections import Counter

S = list(input())
counter = dict(Counter(S))
cnt_v = list(counter.values())

if len(cnt_v) == 2 and cnt_v[0] == 2:
    print('Yes')
else:
    print('No')

