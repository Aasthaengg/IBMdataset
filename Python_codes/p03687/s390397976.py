# https://atcoder.jp/contests/agc016/tasks/agc016_a

from collections import Counter
s = input()
c = Counter(s)
ans = float('inf')
for k, v in c.items():
    # if v < 2:
    #     continue
    t = [-1]
    for i in range(len(s)):
        if s[i] == k:
            t.append(i)
    t.append(len(s))
    temp = []
    for j in range(len(t) - 1):
       temp.append(t[j + 1] - t[j] - 1)
    ans = min(ans, max(temp))
print(ans)