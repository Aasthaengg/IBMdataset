N = int(input())
a = list(map(int, input().split()))

a.sort()

import collections
c = collections.Counter(a)

ans = 0
for i in c.most_common():
    if i[0] <= i[1]:
        ans += i[1] - i[0]
    else:
        ans += i[1]

print(ans)