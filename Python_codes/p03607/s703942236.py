N = int(input())
lis = list()
for i in range(N):
    lis.append(int(input()))

import collections

c = collections.Counter(lis)

ans = 0
for i in c.most_common():
    if i[1] % 2 != 0:
        ans += 1

print(ans)