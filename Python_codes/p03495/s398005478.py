N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

import collections

c = collections.Counter(A)

lis = list()
for i in c.most_common():
    lis.append(i[:][1])

lis.sort()

ans = 0
if len(c.most_common()) > K:
    ans += sum(lis[:(len(c.most_common())- K)])
print(ans)