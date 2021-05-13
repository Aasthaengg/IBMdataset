# -*- coding: utf-8 -*-
N, C = map(int, input().split(' '))
lim = (10 ** 5 + 2) * 2
buf = [0 for _ in range(lim)]

import collections

c_durations_dict = collections.defaultdict(list)
for _ in range(N):
    s, t, c = map(int, input().split(' '))
    c_durations_dict[c].append((s, t))

for durations in c_durations_dict.values():
    durations.sort(key=lambda x: x[0])
    i = 0
    while i < len(durations):
        s1, t1 = durations[i]
        while i + 1 < len(durations) and t1 == durations[i + 1][0]:
            t1 = durations[i + 1][1]
            i += 1

        buf[s1 * 2 - 1] += 1
        buf[t1 * 2] -= 1
        i += 1

ans = 0
for i in range(1, lim):
    buf[i] += buf[i - 1]
    ans = max(ans, buf[i])

print(ans)
