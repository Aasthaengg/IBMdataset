S = input()

import collections

c = collections.Counter(list(S))

ans = "yes"
for i in c.values():
    if i == 1:
        pass
    else:
        ans = "no"
        break

print(ans)