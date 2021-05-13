from copy import copy
from string import ascii_lowercase


s = list(input())
ans = len(s)
for c in ascii_lowercase:
    t = copy(s)
    for i in range(len(s), 0, -1):
        if t == [c] * i:
            ans = min(ans, len(s) - i)
            break
        u = copy(t[:-1])
        for j in range(i - 1):
            if t[j] == c or t[j + 1] == c:
                u[j] = c
            else:
                u[j] = t[j]
        t = u
print(ans)